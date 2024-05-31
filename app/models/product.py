from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import ForeignKey, Integer
from sqlalchemy import String
from sqlalchemy import Text



from .base import Base

from .products_productions_stocks_associated import products_productions_stocks_associated 


if TYPE_CHECKING:
    from .company import Company
    from .type import Type
    from .recipe import Recipe
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

    recipe_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("recipes.id"),
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

    recipe: Mapped["Recipe"] = relationship(
        "Recipe",
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





