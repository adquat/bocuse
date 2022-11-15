from odoo import api, models, fields

class CrmLead(models.Model):
    _inherit = "crm.lead"

    type_evenement = fields.Selection(string="Type d'événement", selection=[
            ('dej', "Déjeuner"),
            ('din', "Dîner"),
        ])
    reunion = fields.Boolean("Réunion", default=False)
    journee_etude = fields.Boolean("Journée d'étude", default=False)
    heures_prevu = fields.Selection(string="Heure repas ou événement", selection=[
        ('12', '12h'),
        ('12-30', '12h30'),
        ('13', '13h'),
        ('19', '19h'),
        ('19-30', '19h30'),
        ('20', '20h'),
        ('20-30', '20h30')
    ])
    nombre_convives = fields.Integer("Nombre de convives")
    dont_enfants = fields.Integer("Dont enfants")
    etablissement_souhaite = fields.Selection(string="Établissement souhaité", selection=[
        ('1', 'Fond Rose'),
        ('2', 'Marguerite')
    ])
    type_occasion = fields.Selection(string="Type d'occasion", selection=[
        ('1', 'Mariage'),
        ('2', 'Anniversaire'),
        ('3', 'Réunion de travail'),
        ('4', 'Autre')
    ])
    autre_occasion = fields.Char("Autre occasion")
    budget_souhaite = fields.Float("Budget souhaité")
    cocktail = fields.Boolean("Cocktail", default=False)
    infos_cocktail1 = fields.Selection(string="Infos Cocktail 1", selection=[
        ('1', 'Cocktail Déjeunatoire'),
        ('2', 'Cocktail Dînatoire'),
        ('3', 'Pièce cocktail à partager')
    ])
    infos_cocktail2 = fields.Selection(string="Infos cocktail 2", selection=[
        ('1', 'Debout en extérieur'),
        ('2', 'Assis en intérieur')
    ])
    date_prestation = fields.Date("Date de la prestation")

    def _prepare_opportunity_quotation_context(self):
        res = super(CrmLead, self)._prepare_opportunity_quotation_context()
        res['default_type_evenement_so'] = self.type_evenement
        res['default_reunion_so'] = self.reunion
        res['default_journee_etude_so'] = self.journee_etude
        res['default_heures_prevu_so'] = self.heures_prevu
        res['default_nombre_convives_so'] = self.nombre_convives
        res['default_dont_enfants_so'] = self.dont_enfants
        res['default_etablissement_souhaite_so'] = self.etablissement_souhaite
        res['default_type_occasion_so'] = self.type_occasion
        res['default_autre_occasion_so'] = self.autre_occasion
        res['default_budget_souhaite_so'] = self.budget_souhaite
        res['default_cocktail_so'] = self.cocktail
        res['default_infos_cocktail1_so'] = self.infos_cocktail1
        res['default_infos_cocktail2_so'] = self.infos_cocktail2
        res['default_date_prestation_so'] = self.date_prestation
        return res


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    type_evenement_so = fields.Selection(string="Type d'événement", selection=[
        ('dej', "Déjeuner"),
        ('din', "Dîner"),
    ])
    reunion_so = fields.Boolean("Réunion", default=False)
    journee_etude_so = fields.Boolean("Journée d'étude", default=False)
    heures_prevu_so = fields.Selection(string="Heure repas ou événement", selection=[
        ('12', '12h30'),
        ('12-30', '12h30'),
        ('13', '13h'),
        ('19', '19h'),
        ('19-30', '19h30'),
        ('20', '20h30'),
        ('20-30', '20h30')
    ])
    nombre_convives_so = fields.Integer("Nombre de convives")
    dont_enfants_so = fields.Integer("Dont enfants")
    etablissement_souhaite_so = fields.Selection(string="Établissement souhaité", selection=[
        ('1', 'Fond Rose'),
        ('2', 'Marguerite')
    ])
    type_occasion_so = fields.Selection(string="Type d'occasion", selection=[
        ('1', 'Mariage'),
        ('2', 'Anniversaire'),
        ('3', 'Réunion de travail'),
        ('4', 'Autre')
    ])
    autre_occasion_so = fields.Char("Autre occasion")
    budget_souhaite_so = fields.Float("Budget souhaité")
    cocktail_so = fields.Boolean("Cocktail", default=False)
    infos_cocktail1_so = fields.Selection(string="Infos Cocktail 1", selection=[
        ('1', 'Cocktail Déjeunatoire'),
        ('2', 'Cocktail Dînatoire'),
        ('3', 'Pièce cocktail à partager')
    ])
    infos_cocktail2_so = fields.Selection(string="Infos cocktail 2", selection=[
        ('1', 'Debout en extérieur'),
        ('2', 'Assis en intérieur')
    ])
    date_prestation_so = fields.Date("Date de la prestation")