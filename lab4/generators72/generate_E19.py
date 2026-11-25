"""E19. История ремонта."""
from datetime import timedelta
from common import add

TABLE = "repair_record"


def generate(cur, batches, rng):
    for b in batches:
        add(cur, TABLE, claim_id=b.claim, record_no=1,
            repaired_on=b.sales[0].day + timedelta(days=22),
            work_description="Диагностика привода и цепи питания", result="Дефект подтверждён")
        add(cur, TABLE, claim_id=b.claim, record_no=2,
            repaired_on=b.sales[0].day + timedelta(days=25),
            work_description="Замена неисправного узла и проверка под нагрузкой",
            result="Исправный товар выдан покупателю")
    return 2 * len(batches)
