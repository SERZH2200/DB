"""E15. Продажи и состав чеков."""
from dataclasses import replace
from datetime import datetime, time, timedelta
from common import Receipt
from common import add

TABLE = "sale"


def generate(cur, batches, rng):
    buyers = ("Анна Попова", "Игорь Павлов", "Роман Егоров", "Олеся Макарова",
              "Елена Волкова", "Илья Титов", "Ирина Галкина", "Виктор Медведев")
    for b in batches:
        tool, part, kit = b.products
        baskets = ([replace(tool, serial=b.serials[0]), replace(part, quantity=2)],
                   [replace(tool, serial=b.serials[1])],
                   [replace(part, quantity=rng.randint(2, 5))],
                   [kit], [replace(part, quantity=rng.randint(1, 3))])
        for index, lines in enumerate(baskets):
            day = b.day + timedelta(days=5 + 8 * index + rng.randrange(4))
            buyer = rng.choice(buyers)
            total = sum(line.quantity * line.retail for line in lines)
            sold_at = datetime.combine(day, time(rng.randrange(9, 20), rng.randrange(60)))
            number = add(cur, TABLE, "sale_id", store_id=b.store, sold_at=sold_at,
                         customer=buyer, total_amount=total, status="проведена")
            b.sales.append(Receipt(number, buyer, day, lines))
    return 5 * len(batches)
