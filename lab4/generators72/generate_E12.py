"""E12. Комплекты расходных материалов."""
from common import add

TABLE = "kit"


def generate(cur, batches, rng):
    for b in batches:
        item = b.products[2]
        add(cur, TABLE, kit_sku=item.sku, composition_version=1,
            kit_name=f"{item.title}, {b.units_per_kit} шт.", formed_on=b.day,
            status="действует")
    return len(batches)
