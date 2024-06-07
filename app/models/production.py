from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Text


from .base import Base
# from .products_productions_stocks_associated import products_productions_stocks_associated


if TYPE_CHECKING:
    from .product import Product
    from .stock import Stock
    from .products_productions_stocks_associated import ProductProductionStockAssociated

class Production(Base):
    
    address: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True,
    )
    description: Mapped[str] = mapped_column(
        Text,
        unique=False,
        nullable=False,
    )
    
    weight_product: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        unique=False,
    )

    weight_stock: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        unique=False,
    )

    assoc_details: Mapped[list["ProductProductionStockAssociated"]] = relationship(
        back_populates="production",
    )

    # products: Mapped[list["Product"]] = relationship(
    #     "Product",
    #     back_populates="productions",
    #     secondary=products_productions_stocks_associated,
    #     overlaps="stocks_m2m",
    # )

    # stocks_m2m: Mapped[list["Stock"]] = relationship(
    #     "Stock",
    #     back_populates="productions",
    #     secondary=products_productions_stocks_associated,
    #     overlaps="products",
    # )

