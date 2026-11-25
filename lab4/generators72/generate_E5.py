"""E5. Поставщики."""
from common import inn_for
from common import add

TABLE = "supplier"


def generate(cur, batches, rng):
    cur.execute("SELECT inn FROM public.supplier")
    occupied = {row[0] for row in cur.fetchall()}
    number = 770000000
    for b in batches:
        while inn_for(number) in occupied:
            number += 1
        inn = inn_for(number)
        number += 1
        b.supplier = add(cur, TABLE, "supplier_id", inn=inn,
                         supplier_name=f"Техноснаб {b.city} {b.category}",
                         requisites="Учебная организация", status="действует",
                         contact_details=f"order-{b.category}@example.org")
    return len(batches)
