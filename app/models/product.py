from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import ForeignKey, Integer
from sqlalchemy import String
from sqlalchemy import Text

from .base import Base

from .products_productions_stocks_associated import products_productions_stocks_associated 


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

    company = relationship(
        "Company",
        uselist=False #what is this??
    )

    type1 = relationship(
        "Type",
        uselist=False,
    )

    recipe = relationship(
        "Recipe",
        uselist=False,
    )


    stocks = relationship(
        "Stock",
        back_populates="product"
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

    stocks_m2m = relationship(
        "Stock",
        back_populates="products",
        secondary=products_productions_stocks_associated,
    )

    productions = relationship(
        "Production",
        back_populates="products",
        secondary=products_productions_stocks_associated,
    )





