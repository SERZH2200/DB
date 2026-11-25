"""E9. Две частичные поставки по одной заявке."""
from datetime import timedelta
from common import add

TABLE = "delivery"


def generate(cur, batches, rng):
    for b in batches:
        for number in (1, 2):
            add(cur, TABLE, contract_id=b.contract, delivery_no=number,
                supplier_id=b.supplier, received_on=b.day + timedelta(days=number),
                responsible_person=b.employee, status="принята")
    return 2 * len(batches)
