from typing import TYPE_CHECKING

from sqlalchemy import JSON
from sqlalchemy import Integer

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


from .base import Base

if TYPE_CHECKING:
    from .product import Product

class Recipe(Base):
    recipe: Mapped[dict] = mapped_column(
        JSON,
        unique=False,
        nullable=False,
    )

    products: Mapped[list["Product"]] = relationship(
        "Product",
        back_populates="recipe",
    )


