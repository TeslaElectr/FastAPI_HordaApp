from .base import Base

from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text


class Type(Base):
    
    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        unique=True,
    )

    products = relationship(
        "Product",
        back_populates="type1"
    )