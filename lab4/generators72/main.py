import argparse
from datetime import date, timedelta
from getpass import getpass
from importlib import import_module
import os
import random
import sys
from uuid import uuid4

import psycopg

from common import Batch


# Сначала справочники и документы, затем их зависимые строки.
ORDER = (1, 2, 3, 4, 5, 6, 18, 7, 8, 9, 10, 23, 11, 12, 13, 14,
         15, 21, 16, 22, 17, 19, 20)
CITIES = (("Москва", "Москва"), ("Тула", "Тульская область"),
          ("Химки", "Московская область"), ("Калуга", "Калужская область"))
STAFF = ("Мария Зотова", "Максим Котов", "Алина Ильина", "Виктор Лебедев",
         "Ольга Петрова", "Елена Борисова")
FAMILIES = (("Дрель", "Сверло"), ("Лобзик", "Пилка"),
            ("Шуруповёрт", "Бита"), ("Шлифмашина", "Шлифовальный круг"))


def run(conn, amount, seed):
    rng = random.Random(seed)
    tag = uuid4().hex[:10]
    batches = []
    for number in range(1, amount + 1):
        city, region = rng.choice(CITIES)
        day = date(2024, 1, 1) + timedelta(days=rng.randrange(600))
        batches.append(Batch(number, tag, day, city, region, rng.choice(STAFF),
                             rng.choice(FAMILIES), units_per_kit=rng.randint(2, 5)))

    counts = {}
    with conn.transaction(), conn.cursor() as cursor:
        cursor.execute("LOCK TABLE public.product_instance IN SHARE ROW EXCLUSIVE MODE")
        for entity in ORDER:
            module = import_module(f"generate_E{entity}")
            counts[module.TABLE] = module.generate(cursor, batches, rng)
            if counts[module.TABLE] < amount:
                raise RuntimeError(f"E{entity}: создано слишком мало строк")
    return counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rows", type=int, default=500,
                        help="минимум новых строк на таблицу (по умолчанию 500)")
    parser.add_argument("--seed", type=int, default=72, help="начальное число для random")
    args = parser.parse_args()
    if args.rows < 500:
        parser.error("--rows должен быть не меньше 500")
    settings = dict(host=os.getenv("PGHOST", "127.0.0.1"), port=os.getenv("PGPORT", "5432"),
                    dbname=os.getenv("PGDATABASE", "lab4_db"), user=os.getenv("PGUSER", "lab4_user"))
    if not (os.getenv("PGPASSWORD") or os.getenv("PGPASSFILE")):
        password = getpass("Пароль PostgreSQL (Enter для .pgpass): ")
        if password:
            settings["password"] = password
    try:
        with psycopg.connect(**settings) as conn:
            counts = run(conn, args.rows, args.seed)
    except (psycopg.Error, ValueError, RuntimeError) as exc:
        print(f"Ошибка загрузки: {exc}", file=sys.stderr)
        return 1
    for table, count in counts.items():
        print(f"{table:26} +{count}")
    print(f"Добавлено строк: {sum(counts.values())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
