from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import Float, ForeignKey, Integer
from sqlalchemy import Text

from .products_productions_stocks_associated import products_productions_stocks_associated
from .base import Base

if TYPE_CHECKING:
    from .company import Company
    from .product import Product
    from .type import Type
    from .stock import Stock
    from .production import Production
    from .products_productions_stocks_associated import ProductProductionStockAssociated

class Stock(Base):
    
    weight: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        unique=False,
    )
    description: Mapped[str] = mapped_column(
        Text,
        unique=False,
        nullable=False,
    )
    price: Mapped[float] = mapped_column(
        Float,
        unique=False,
        nullable=False,
    )

    company_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("companys.id"),
        nullable=False,
        unique=False,
    )

    product_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("products.id"),
        nullable=False,
        unique=False,
    )

    company: Mapped["Company"] = relationship(
        "Company",
        back_populates="stocks",
    )

    product: Mapped["Product"] = relationship(
        "Product",
        back_populates="stocks",
    )

    assoc_details: Mapped[list["ProductProductionStockAssociated"]] = relationship(
        back_populates="stock",
    )


    # products: Mapped[list["Product"]] = relationship(
    #     "Product",
    #     back_populates="stocks_m2m",
    #     secondary=products_productions_stocks_associated,
    #     overlaps="productions",
    # )
    
    # productions: Mapped[list["Production"]] = relationship(
    #     "Production",
    #     back_populates="stocks_m2m",
    #     secondary=products_productions_stocks_associated,
    #     overlaps="products",
    # )
