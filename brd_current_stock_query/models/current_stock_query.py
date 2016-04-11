# -*- coding: utf-8 -*-
# © 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields
from openerp.tools import drop_view_if_exists


class CurrentStockQuery(models.Model):
    _name = "brd.current_stock_query"
    _description = "Current Stock Query"
    _auto = False

    product_id = fields.Many2one(
        string="Product",
        comodel_name="product.product",
        )

    location_id = fields.Many2one(
        string="Location",
        comodel_name="stock.location",
        )

    lot_id = fields.Many2one(
        string="Lot",
        comodel_name="stock.production.lot",
        )

    quantity = fields.Float(
        string="Quantity",
        )

    def _auto_init(self, cr, context=None):
        drop_view_if_exists(cr, self._table)
        strSQL = """
            CREATE OR REPLACE VIEW %(table)s AS (
                SELECT  row_number() OVER() AS id,
                        a.product_id AS product_id,
                        a.location_id AS location_id,
                        a.lot_id AS lot_id,
                        SUM(a.qty) AS quantity
                FROM    stock_quant AS a
                JOIN    product_product AS b ON a.product_id = b.id
                WHERE   b.active = True
                GROUP BY    a.product_id, 
                            a.location_id,
                            a.lot_id

                )
        """ % {'table': self._table}

        cr.execute(strSQL)

        return super(CurrentStockQuery, self)._auto_init(
            cr, context=context)
    

