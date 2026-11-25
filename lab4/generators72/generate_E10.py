"""E10. Распределения поставок по заявкам."""
from datetime import timedelta
from common import add

TABLE = "delivery_allocation"


def generate(cur, batches, rng):
    for b in batches:
        for number in (1, 2):
            allocation = add(cur, TABLE, "allocation_id", store_id=b.store, request_id=b.request,
                             contract_id=b.contract, delivery_no=number,
                             allocated_on=b.day + timedelta(days=number), status="передано магазину")
            b.allocations.append(allocation)
    return 2 * len(batches)
