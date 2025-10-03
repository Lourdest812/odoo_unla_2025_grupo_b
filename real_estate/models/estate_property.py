<<<<<<< HEAD
from odoo import models, fields
from datetime import timedelta

=======
from odoo import models, fields, api
from datetime import timedelta
from odoo.exceptions import UserError
>>>>>>> feature/real_estate_U2-16

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Propiedades"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Descripcion")
    postcode = fields.Char(string="Codigo Postal")

<<<<<<< HEAD
    # a) Tipo Propiedad -> estate.property.type
=======
>>>>>>> feature/real_estate_U2-16
    property_type_id = fields.Many2one(
        "estate.property.type",
        string="Tipo Propiedad",
        ondelete="set null",
        index=True,
    )

<<<<<<< HEAD
    # b) Comprador -> res.partner
=======
>>>>>>> feature/real_estate_U2-16
    buyer_id = fields.Many2one(
        "res.partner",
        string="Comprador",
        ondelete="set null",
        index=True,
    )

<<<<<<< HEAD
    # c) Vendedor -> res.users | no copiar al duplicar | default = usuario logueado
=======
>>>>>>> feature/real_estate_U2-16
    salesman_id = fields.Many2one(
        "res.users",
        string="Vendedor",
        default=lambda self: self.env.user,
        copy=False,
        ondelete="set null",
        index=True,
    )

    tag_ids = fields.Many2many(
        comodel_name="estate.property.tag",
        relation="estate_property_tag_rel",
        column1="property_id",
        column2="tag_id",
        string="Etiquetas",
    )

    offer_ids = fields.One2many(
        comodel_name="estate.property.offer",
        inverse_name="property_id",
        string="Ofertas",
    )

<<<<<<< HEAD
    # Fecha por defecto: hoy + 3 meses (~90 días)
=======
>>>>>>> feature/real_estate_U2-16
    date_availability = fields.Date(
        string="Fecha de disponibilidad",
        default=lambda self: fields.Date.today() + timedelta(days=90),
        copy=False,
    )

    expected_price = fields.Float(string="Precio esperado")
<<<<<<< HEAD

    # No copiar al duplicar
    sellind_price = fields.Float(string="Precio de venta", copy=False)

    bedrooms = fields.Integer(string="Habitaciones", default=2)
    living_area = fields.Integer(string="Superficie Cubierta")
    Facade = fields.Integer(string="Fachadas")
=======
    selling_price = fields.Float(string="Precio de venta", copy=False)

    bedrooms = fields.Integer(string="Habitaciones", default=2)
    living_area = fields.Integer(string="Superficie Cubierta")
    facade = fields.Integer(string="Fachadas")
>>>>>>> feature/real_estate_U2-16
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Jardin")
    garden_orientation = fields.Selection(
        selection=[("north", "Norte"), ("south", "Sur"), ("east", "Este"), ("west", "Oeste")],
        default="north",
        string="Orientacion del jardin",
    )
    garden_area = fields.Integer(string="Superficie del jardin")

    state = fields.Selection(
        selection=[
            ("new", "Nuevo"),
            ("offer_received", "Oferta recibida"),
            ("offer_accepted", "Oferta aceptada"),
            ("sold", "Vendido"),
            ("canceled", "Cancelado"),
        ],
        default="new",
        copy=False,
        string="Estado",
        required=True,
    )
<<<<<<< HEAD
=======


    def action_sold(self):
        for rec in self:
            if rec.state == 'canceled':
                raise UserError("No se puede marcar como vendida una propiedad cancelada")
            rec.state = 'sold'

    def action_cancel(self):
        for rec in self:
            if rec.state == 'sold':
                raise UserError("No se puede cancelar una propiedad vendida")
            rec.state = 'canceled'

    total_area = fields.Float(
        string='Superficie total',
        compute='_compute_total_area',
        store=True
    )

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = (record.living_area or 0) + (record.garden_area or 0)

    best_offer = fields.Float(
        string='Mejor oferta',
        compute='_compute_best_offer',
        store=True
    )

    @api.depends('offer_ids.price')
    def _compute_best_offer(self):
        for rec in self:
            offers = rec.offer_ids.mapped('price')
            rec.best_offer = max(offers) if offers else 0

    @api.onchange('garden')
    def _onchange_garden(self):
        for record in self:
            if record.garden:
                record.garden_area = 10
            else:
                record.garden_area = 0

    @api.onchange('expected_price')
    def _onchange_expected_price(self):
        for record in self:
            if record.expected_price and record.expected_price < 10000:
                return {
                    'warning': {
                        'title': "Precio bajo",
                        'message': "El precio esperado es menor a 10.000. Por favor, verifica si ingresaste el valor correctamente.",
                    }
                }
>>>>>>> feature/real_estate_U2-16
