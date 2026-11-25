"""E8. Заявки на пополнение."""
from datetime import datetime, time
from common import add

TABLE = "store_request"


def generate(cur, batches, rng):
    for b in batches:
        tool, part, _ = b.products
        request = f"{tool.sku}: 2 шт.; {part.sku}: 30 шт."
        b.request = add(cur, TABLE, "request_id", store_id=b.store,
                        requested_at=datetime.combine(b.day, time(9, 15)), applicant=b.employee,
                        request_contents=request, status="исполнена", responsible_person=b.employee)
    return len(batches)
