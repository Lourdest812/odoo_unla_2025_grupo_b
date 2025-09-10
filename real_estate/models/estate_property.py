from odoo import models, fields
from datetime import timedelta


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Propiedades"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Descripcion")
    postcode = fields.Char(string="Codigo Postal")

    # a) Tipo Propiedad -> estate.property.type
    property_type_id = fields.Many2one(
        "estate.property.type",
        string="Tipo Propiedad",
        ondelete="set null",
        index=True,
    )

    # b) Comprador -> res.partner
    buyer_id = fields.Many2one(
        "res.partner",
        string="Comprador",
        ondelete="set null",
        index=True,
    )

    # c) Vendedor -> res.users | no copiar al duplicar | default = usuario logueado
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

    # Fecha por defecto: hoy + 3 meses (~90 días)
    date_availability = fields.Date(
        string="Fecha de disponibilidad",
        default=lambda self: fields.Date.today() + timedelta(days=90),
        copy=False,
    )

    expected_price = fields.Float(string="Precio esperado")

    # No copiar al duplicar
    sellind_price = fields.Float(string="Precio de venta", copy=False)

    bedrooms = fields.Integer(string="Habitaciones", default=2)
    living_area = fields.Integer(string="Superficie Cubierta")
    Facade = fields.Integer(string="Fachadas")
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
