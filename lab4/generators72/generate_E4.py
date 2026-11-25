"""E4. Значения характеристик."""
from common import add

TABLE = "product_attribute_value"


def generate(cur, batches, rng):
    for b in batches:
        for item in b.products:
            add(cur, TABLE, sku=item.sku, attribute_id=b.attribute,
                attribute_value=f"М-{b.category}", unit=None)
    return 3 * len(batches)
