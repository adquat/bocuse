# -*- coding: utf-8 -*-

from odoo import models, fields, api
from lxml import etree
import simplejson

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    version = fields.Integer('Version', default=1)
    parent_version_id = fields.Many2one('sale.order', string='Sale order parent', ondelete='set null',)
    state = fields.Selection(selection_add=[('archive', 'Archive')])
    version_count = fields.Integer(compute="_compute_version_count", string='Version Count', copy=False,
                                   default=0, store=True)
    active = fields.Boolean('Active', default=True)

    _sql_constraints = [
        ('name_unique', 'unique(name, version, company_id)', 'Order Reference must be unique per Company!'),
    ]

    def button_create_new_version(self):
        self.ensure_one()
        if self.state in ('draft', 'sent'):
            parent_id = self.parent_version_id.id or self.id
            new_so = self.copy({'version': self.version + 1,
                                'state': 'draft',
                                'name': self.name,
                                'parent_version_id': parent_id})
            self.state = 'archive'
            self.active = False
            return {
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'sale.order',
                'type': 'ir.actions.act_window',
                'res_id': new_so.id,
            }

        return True

    def copy(self, default=None):
        if default is None:
            default = {}
        if not 'version' in default:
            default['parent_version_id'] = False
            default['version'] = 1
        return super(SaleOrder, self).copy(default)

    @api.depends('name', 'version',)
    def _compute_display_name(self):
        for so in self:
            so.display_name = "%s-%s" % (so.name, so.version)

    def action_view_version(self):
        self.ensure_one()
        if self.parent_version_id:
            action = self.env.ref('sale.action_orders').read()[0]
            action['domain'] = [('name', '=', self.name),
                                '|', ('active', '=', False), ('active', '=', True)]
            action['context'] = {'turn_view_readonly': True}
        else:
            action = {'type': 'ir.actions.act_window_close'}
        return action

    @api.depends('parent_version_id')
    def _compute_version_count(self):
        parent_count = {}
        for order in self:
            parent_id = order.parent_version_id and order.parent_version_id.id
            if parent_id:
                if parent_id not in parent_count:
                    parent_count[order.id] = self.search([('name', '=', order.name),
                                                          '|', ('active', '=', False), ('active', '=', True)],
                                                         count=True)
            order.version_count = parent_count.get(order.id, 0)

    @api.model
    def fields_view_get(self, view_id=None, view_type=False, toolbar=False, submenu=False):
        context = self._context
        res = super(SaleOrder, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar,
                                                     submenu=submenu)

        if context.get('turn_view_readonly'):  # Check for context value
            doc = etree.XML(res['arch'])
            if view_type == 'form':            # Applies only for form view
                for node in doc.xpath("//field"):   # All the view fields to readonly
                    node.set('readonly', '1')
                    modifiers = simplejson.loads(node.get("modifiers"))
                    modifiers['readonly'] = True
                    node.set("modifiers", simplejson.dumps(modifiers))

                res['arch'] = etree.tostring(doc)
        return res
