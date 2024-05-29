from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Integer
from sqlalchemy import String

from .base import Base

if TYPE_CHECKING:
    from .company import Company

class Warehouse(Base):
    address: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True,
    )

    phone: Mapped[int] = mapped_column(
        Integer,
        unique=False,
        nullable=True,
    )

    company_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("companys.id"),
        unique=False,
        nullable=False,
    )

    company: Mapped["Company"] = relationship(
        "Company",
        back_populates="warehouses",
    )