"""E22. Позиции возвратов."""
from common import add

TABLE = "return_item"


def generate(cur, batches, rng):
    for b in batches:
        for number, sale in zip(b.returns, b.sales[1:3]):
            add(cur, TABLE, return_id=number, line_no=1, sale_id=sale.number,
                sale_line_no=1, quantity=1, unit_price=sale.lines[0].retail)
    return 2 * len(batches)
