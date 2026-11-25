"""E11. Серийные экземпляры."""
from datetime import timedelta
from common import add

TABLE = "product_instance"


def generate(cur, batches, rng):
    cur.execute("SELECT COALESCE(MAX(serial_number), 0) FROM public.product_instance")
    serial = max(0, cur.fetchone()[0])
    if serial + 2 * len(batches) > 2147483647:
        raise ValueError("Недостаточно свободных серийных номеров типа integer.")
    for b in batches:
        for number in (1, 2):
            serial += 1
            add(cur, TABLE, serial_number=serial, sku=b.products[0].sku,
                received_on=b.day + timedelta(days=number), current_location="У покупателя",
                status="продан")
            b.serials.append(serial)
    return 2 * len(batches)
