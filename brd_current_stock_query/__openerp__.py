# -*- coding: utf-8 -*-
# © 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Brodo - Current Stock Query",
    "version": "8.0.1.0.0",
    "category": "Warehouse",
    "website": "https://opensynergy-indonesia.com",
    "author": "Andhitia Rama, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "stock",
        "brd_warehouse_reporting",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/data_Groups.xml",
        "views/current_stock_query_views.xml",
        "menu/menu_Report.xml",
    ],
}
