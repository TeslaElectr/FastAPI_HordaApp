from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import ForeignKey, Integer
from sqlalchemy import String
from sqlalchemy import Text



from .base import Base

from .products_productions_stocks_associated import products_productions_stocks_associated 
from .products_products_associated import products_products_associated 


if TYPE_CHECKING:
    from .company import Company
    from .type import Type
    from .stock import Stock
    from .production import Production

class Product(Base):
    
    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True,
    )
    description: Mapped[str] = mapped_column(
        Text,
        unique=False,
        nullable=False,
    )

    company_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("companys.id"),
        nullable=False,
        unique=False,
    )

    type_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("types.id"),
        nullable=False,
        unique=False,
    )

    company: Mapped["Company"] = relationship(
        "Company",
        back_populates="products",
    )

    type1: Mapped["Type"] = relationship(
        "Type",
        back_populates="products",
    )

    stocks: Mapped[list["Stock"]] = relationship(
        "Stock",
        back_populates="product"
    )

    stocks_m2m: Mapped[list["Stock"]] = relationship(
        "Stock",
        back_populates="products",
        secondary=products_productions_stocks_associated,
        overlaps="productions",
    )

    productions: Mapped[list["Production"]] = relationship(
        "Production",
        back_populates="products",
        secondary=products_productions_stocks_associated,
        overlaps="stocks_m2m",
    )


    target_products: Mapped[list["Product"]] = relationship(
        "Product",
        back_populates="row_products",
        secondary=products_products_associated,
        primaryjoin="Product.id == products_products_associated.c.product_target_id",
        secondaryjoin="Product.id == products_products_associated.c.product_id",
        foreign_keys="[products_products_associated.c.product_target_id, products_products_associated.c.product_id]"
    )

    row_products: Mapped[list["Product"]] = relationship(
        "Product",
        back_populates="targer_products",
        secondary=products_products_associated,
        primaryjoin="Product.id == products_products_associated.c.product_id",
        secondaryjoin="Product.id == products_products_associated.c.product_target_id",
        foreign_keys="[products_products_associated.c.product_id, products_products_associated.c.product_target_id]"
    )




