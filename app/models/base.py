from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import declared_attr

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy import Integer


class Base(DeclarativeBase):

    @declared_attr.directive
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    
    def __str__(self) -> str:
        return f"- {self.__class__.__name__}: {self.__name__}"

        
    def __repr__(self) -> str:
        return self.__str__()