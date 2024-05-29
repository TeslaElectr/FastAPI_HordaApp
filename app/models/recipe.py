from .base import Base

from sqlalchemy import JSON
from sqlalchemy import Integer

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Recipe(Base):
    recipe: Mapped[dict] = mapped_column(
        JSON,
        unique=False,
        nullable=False,
    )

    products = relationship(
        "Product",
        back_populates="recipe",
    )


