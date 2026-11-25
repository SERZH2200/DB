"""E17. Гарантийные обращения."""
from datetime import timedelta
from common import add

TABLE = "warranty_claim"


def generate(cur, batches, rng):
    faults = ("Не включается", "Перегрев при штатной нагрузке", "Нестабильная работа привода")
    for b in batches:
        sale = b.sales[0]
        b.claim = add(cur, TABLE, "claim_id", serial_number=sale.lines[0].serial,
                      customer=sale.buyer, claimed_on=sale.day + timedelta(days=20),
                      fault_description=rng.choice(faults), warranty_terms="12 месяцев",
                      status="закрыто", decision="Гарантийный ремонт выполнен")
    return len(batches)
