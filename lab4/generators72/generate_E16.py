"""E16. Возвраты с разными исходами."""
from datetime import datetime, time, timedelta
from common import add

TABLE = "sale_return"


def generate(cur, batches, rng):
    for b in batches:
        # Вторая продажа: предъявлен другой экземпляр. Третья: возврат одной единицы.
        for sale, reason, status in ((b.sales[1], "Несовпадение серийного номера", "отказано"),
                                     (b.sales[2], "Дефект расходного материала", "одобрено")):
            day = sale.day + timedelta(days=3)
            number = add(cur, TABLE, "return_id", sale_id=sale.number, store_id=b.store,
                         returned_at=datetime.combine(day, time(14, 30)), reason=reason,
                         responsible_person=b.employee, status=status, total_amount=sale.lines[0].retail)
            b.returns.append(number)
    return 2 * len(batches)
