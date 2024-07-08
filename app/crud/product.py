from typing import Optional
from sqlalchemy import delete
from sqlalchemy import select
from sqlalchemy import Result

from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Product

from app.schemas import ProductCreateSchema2
from app.schemas import ProductCreateSchema

from app.exceptions import PydanticDumpException
from app.exceptions import DataBaseConnectionError


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
    ) -> Optional[Product]:

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
        print(e)
        raise PydanticDumpException()

    session.add(product)

    try:
        await session.commit()
    except Exception as e:
        print(e)
        raise DataBaseConnectionError()

    return product

    
async def create_products(
    session: AsyncSession,
    create_products: list[ProductCreateSchema2],
    ):

    try:
        products = [
            Product(**product.model_dump())
            for product in create_products
        ]
    except Exception as e:
        print(e)
        raise PydanticDumpException()


    session.add_all(products)

    
    try:
        await session.commit()
    except Exception as e:
        print(e)
        raise DataBaseConnectionError()

        
    return products
    
async def delete_all_products(
    session: AsyncSession,
    ) -> None:
    
    stmt = (
        delete(Product)
    )

    await session.execute(stmt)
    await session.commit()



    
    


    
    