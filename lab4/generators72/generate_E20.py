"""E20. Акты при расхождении серийных номеров."""
from datetime import timedelta
from common import add

TABLE = "discrepancy_report"


def generate(cur, batches, rng):
    for b in batches:
        sale = b.sales[1]
        serial = sale.lines[0].serial
        add(cur, TABLE, return_id=b.returns[0], reported_on=sale.day + timedelta(days=3),
            sold_serial_number=str(serial), returned_serial_number=f"X-{serial}",
            discrepancy_description="Предъявленный экземпляр отличается от указанного в чеке.")
    return len(batches)
