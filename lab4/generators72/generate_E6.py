"""E6. Договоры поставки."""
from datetime import timedelta
from common import add

TABLE = "supply_contract"


def generate(cur, batches, rng):
    for b in batches:
        b.contract = add(cur, TABLE, "contract_id", supplier_id=b.supplier,
                         signed_on=b.day - timedelta(days=10), valid_from=b.day,
                         valid_to=None, terms="Оплата в течение 15 дней после приёмки",
                         status="действует")
    return len(batches)
