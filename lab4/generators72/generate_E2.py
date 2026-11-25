"""E2. Товары."""
from decimal import Decimal
from common import Position
from common import add

TABLE = "product"


def generate(cur, batches, rng):
    for b in batches:
        tool, part = b.family
        model = f"М-{b.category}"
        unit_price = rng.randint(40, 220)
        items = (("T", tool, "серийный", rng.randrange(3500, 19000, 50)),
                 ("P", part, "количественный", unit_price),
                 ("K", "Набор: " + part, "количественный", unit_price * b.units_per_kit))
        for prefix, title, mode, price in items:
            sku = f"{prefix}-{b.category}"
            item = Position(sku, f"{title} {model}", Decimal(price), Decimal(price) * Decimal("0.70"))
            add(cur, TABLE, sku=sku, category_id=b.category, tracking_method=mode,
                product_name=item.title, status="в продаже")
            b.products.append(item)
    return 3 * len(batches)
