"""E7. Закупочные цены по договорам."""
from common import add

TABLE = "purchase_price"


def generate(cur, batches, rng):
    for b in batches:
        for item in b.products[:2]:
            add(cur, TABLE, contract_id=b.contract, sku=item.sku, valid_from=b.day,
                valid_to=None, amount=item.purchase, currency="RUB")
    return 2 * len(batches)
