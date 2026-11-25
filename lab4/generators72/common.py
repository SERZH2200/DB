from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal
from functools import lru_cache

from psycopg import sql


@dataclass
class Position:
    sku: str
    title: str
    retail: Decimal
    purchase: Decimal
    serial: int | None = None
    quantity: int = 1


@dataclass
class Receipt:
    number: int
    buyer: str
    day: date
    lines: list[Position]


@dataclass
class Batch:
    """Набор связанных данных по одной товарной серии и одному магазину."""
    number: int
    tag: str
    day: date
    city: str
    region: str
    employee: str
    family: tuple[str, str]
    category: int = 0
    attribute: int = 0
    supplier: int = 0
    contract: int = 0
    store: int = 0
    request: int = 0
    claim: int = 0
    units_per_kit: int = 2
    products: list[Position] = field(default_factory=list)
    allocations: list[int] = field(default_factory=list)
    serials: list[int] = field(default_factory=list)
    sales: list[Receipt] = field(default_factory=list)
    returns: list[int] = field(default_factory=list)


@lru_cache(maxsize=None)
def insert_query(table, columns, returning):
    query = sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(
        sql.Identifier("public", table),
        sql.SQL(", ").join(map(sql.Identifier, columns)),
        sql.SQL(", ").join(sql.Placeholder() for _ in columns),
    )
    if returning:
        query += sql.SQL(" RETURNING {}").format(sql.Identifier(returning))
    return query


def add(cursor, table, returning=None, **values):
    cursor.execute(insert_query(table, tuple(values), returning), tuple(values.values()))
    if returning:
        return cursor.fetchone()[0]


def inn_for(number):
    digits = f"{number:09d}"
    if len(digits) != 9:
        raise ValueError("Для учебного десятизначного ИНН исчерпан диапазон номеров.")
    weights = (2, 4, 10, 3, 5, 9, 4, 6, 8)
    check = sum(int(d) * w for d, w in zip(digits, weights)) % 11 % 10
    return digits + str(check)
