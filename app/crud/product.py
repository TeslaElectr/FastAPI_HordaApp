
from sqlalchemy import select
from sqlalchemy import Result

from sqlalchemy.ext.asyncio import AsyncSession

from models import Product
from schemas import ProductCreateSchema
from exceptions import PydanticDumpException
from exceptions import DataBaseConnectionError


async def get_all_products(
    session: AsyncSession
    ) -> list[Product]:

    stmt = (
        select(Product)        
        .order_by(Product.id)
    )
    
    try:
        result: Result = await session.execute(stmt)
    except Exception as e:
        print(e)
        raise DataBaseConnectionError()

    products = list(result.scalars().all())

    return products


async def get_proudct_by_id(
    session: AsyncSession,
    product_id: int,
    ) -> Product:

    stmt = (
        select(Product)
        .where(Product.id == product_id)
    )

    try:
        result: Result = await session.execute(stmt)
    except Exception as e:
        print(e)
        raise DataBaseConnectionError()

    product = result.scalar_one_or_none()

    return product
    

async def create_product(
    session: AsyncSession,
    product_create: ProductCreateSchema,
    company_id: int,
    type_id: int,
) -> Product:
    
    try:
        product = Product(
            **product_create.model_dump(),
            company_id=company_id,
            type_id=type_id,
        )
    except Exception as e:
        raise PydanticDumpException(
            f"error with commit company {e.errors()}"
            )

    session.add(product)

    try:
        await session.commit()
    except Exception as e:
        raise DataBaseConnectionError(
            f"error commit db {e.errors()}"
            )

    return product

    
    