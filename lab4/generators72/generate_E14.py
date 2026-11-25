"""E14. История розничных цен."""
from datetime import timedelta
from decimal import Decimal
from common import add

TABLE = "retail_price"


def generate(cur, batches, rng):
    for b in batches:
        for item in b.products:
            add(cur, TABLE, sku=item.sku, region=b.region, valid_from=b.day - timedelta(days=30),
                valid_to=b.day - timedelta(days=1), amount=item.retail * Decimal("0.95"),
                currency="RUB")
            add(cur, TABLE, sku=item.sku, region=b.region, valid_from=b.day, valid_to=None,
                amount=item.retail, currency="RUB")
    return 6 * len(batches)
