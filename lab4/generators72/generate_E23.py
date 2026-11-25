"""E23. Состав каждого распределения."""
from common import add

TABLE = "delivery_allocation_item"


def generate(cur, batches, rng):
    for b in batches:
        for allocation in b.allocations:
            for item, quantity in zip(b.products[:2], (1, 15)):
                add(cur, TABLE, allocation_id=allocation, sku=item.sku, quantity=quantity)
    return 4 * len(batches)
