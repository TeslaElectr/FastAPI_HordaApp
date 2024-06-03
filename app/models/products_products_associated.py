from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy import FLOAT

from .base import Base


products_products_associated = Table(
    "products_products_associated",
    Base.metadata,
    Column("poroduct_targer_id", ForeignKey("products.id"), primary_key=True),
    Column("product_id", ForeignKey("products.id"), primary_key=True),
    Column("percent", FLOAT, nullable=False, unique=False),
    Column("losses", FLOAT, nullable=False, unique=False),
)

