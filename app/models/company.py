from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import Integer
from sqlalchemy import BigInteger
from sqlalchemy import String

from .base import Base


if TYPE_CHECKING:
    from .warehouse import Warehouse
    from .product import Product
    from .stock import Stock



class Company(Base):
    
    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True,
    )
    city: Mapped[str] = mapped_column(
        String,
        unique=False,
        nullable=False,
    )
    inn: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        nullable=True,
    )

    kpp: Mapped[int] = mapped_column(
        BigInteger,
        nullable=True,
        unique=True,
    )
    address: Mapped[str] = mapped_column(
        String,
        unique=False,
        nullable=True,
    )

    phone: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        nullable=True,
    )

    email: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=True,
    )

    products: Mapped[list["Product"]] = relationship(
        "Product",
        back_populates="company",
    )

    stocks: Mapped[list["Stock"]] = relationship(
        "Stock",
        back_populates="company",
    )

    warehouses: Mapped[list["Warehouse"]] = relationship(
        "Warehouse",
        back_populates="company",
    )