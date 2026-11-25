"""E3. Характеристики."""
from common import add

TABLE = "product_attribute"


def generate(cur, batches, rng):
    for b in batches:
        b.attribute = add(cur, TABLE, "attribute_id", category_id=b.category,
                          attribute_name="Модельная серия", value_type="строка",
                          unit=None, is_required=True)
    return len(batches)
