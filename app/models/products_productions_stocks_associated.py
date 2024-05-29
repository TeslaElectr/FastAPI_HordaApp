from sqlalchemy import Column, Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column


from .base import Base


products_productions_stocks_associated = Table(
    "products_productions_stocks_associated",
    Base.metadata,
    Column("products_id", ForeignKey("products.id"), primary_key=True),
    Column("productions_id", ForeignKey("productions.id"), primary_key=True),
    Column("stocks_id", ForeignKey("stocks.id"), primary_key=True),
)