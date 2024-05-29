from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import Integer
from sqlalchemy import String

from .base import Base

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
        Integer,
        unique=True,
        nullable=True,
    )

    kpp: Mapped[int] = mapped_column(
        Integer,
        nullable=True,
        unique=True,
    )
    address: Mapped[str] = mapped_column(
        String,
        unique=False,
        nullable=True,
    )

    phone: Mapped[int] = mapped_column(
        Integer,
        unique=True,
        nullable=True,
    )

    email: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=True,
    )

    products = relationship(
        "Product",
        back_populates="company",
    )

    stocks = relationship(
        "Stock",
        back_populates="company",
    )

    warehouses = relationship(
        "Warehouse",
        back_populates="company",
    )