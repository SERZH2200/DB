"""E18. Магазины."""
from common import add

TABLE = "store"


def generate(cur, batches, rng):
    for b in batches:
        b.store = add(cur, TABLE, "store_id", store_name=f"{b.city} — Мастер {b.category}",
                      address=f"{b.city}, ул. Торговая, д. {b.number}",
                      region=b.region, status="открыт")
    return len(batches)
