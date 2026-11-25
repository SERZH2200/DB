"""E21. Позиции продаж."""
from common import add

TABLE = "sale_item"


def generate(cur, batches, rng):
    count = 0
    for b in batches:
        for sale in b.sales:
            for number, line in enumerate(sale.lines, start=1):
                add(cur, TABLE, sale_id=sale.number, line_no=number, serial_number=line.serial,
                    sku=line.sku, quantity=line.quantity, unit_price=line.retail)
                count += 1
    return count
