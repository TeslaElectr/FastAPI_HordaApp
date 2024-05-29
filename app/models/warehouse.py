from .base import Base

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Integer
from sqlalchemy import String


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

    company = relationship(
        "Company",
        uselist=False,
    )