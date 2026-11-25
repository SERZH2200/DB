"""E1. Категории каталога."""
from common import add

TABLE = "product_category"


def generate(cur, batches, rng):
    for index, b in enumerate(batches):
        # Каждые десять категорий образуют группу с общим родителем.
        parent = batches[index - index % 10].category if index % 10 else None
        name = f"{b.family[0]} и оснастка {b.tag}-{b.number}"
        b.category = add(cur, TABLE, "category_id", parent_category_id=parent,
                         category_name=name, description="Каталожная серия " + str(b.number))
    return len(batches)
