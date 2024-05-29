from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import Float, ForeignKey, Integer
from sqlalchemy import Text

from .products_productions_stocks_associated import products_productions_stocks_associated
from .base import Base

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

    company = relationship(
        "Company",
        uselist=False, #what is this??
    )

    product = relationship(
        "Product",
        uselist=False,
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

    products = relationship(
        "Product",
        back_populates="stocks_m2m",
        secondary=products_productions_stocks_associated,
    )
    
    productions = relationship(
        "Production",
        back_populates="stocks_m2m",
        secondary=products_productions_stocks_associated,
    )
