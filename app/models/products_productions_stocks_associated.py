from typing import TYPE_CHECKING

from sqlalchemy import Table
from sqlalchemy import Integer
from sqlalchemy import Column
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .base import Base

if TYPE_CHECKING:
    from .product import Product
    from .production import Production
    from .stock import Stock


class ProductProductionStockAssociated(Base):
    product_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("products.id"),
        primary_key=True
        )

    production_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("productions.id"),
        primary_key=True
        )
    
    stock_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("stocks.id"),
        primary_key=True
        )

    product: Mapped["Product"] = relationship(back_populates="assoc_details")
    stock: Mapped["Stock"] = relationship(back_populates="assoc_details")
    production: Mapped["Production"] = relationship(back_populates="assoc_details")
    

        
    

# products_productions_stocks_associated = Table(
#     "products_productions_stocks_associated",
#     Base.metadata,
#     Column("products_id", ForeignKey("products.id"), primary_key=True),
#     Column("productions_id", ForeignKey("productions.id"), primary_key=True),
#     Column("stocks_id", ForeignKey("stocks.id"), primary_key=True),
# )