# Copyright 2019 Eficent <http://www.eficent.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade

def fill_stock_warehouse_picking_types(env):
    warehouse_ids = env['stock.warehouse'].search([])
    for warehouse_id in warehouse_ids:
        warehouse_id._create_or_update_sequences_and_picking_types()

@openupgrade.migrate()
def migrate(env, version):
    fill_stock_warehouse_picking_types(env)
