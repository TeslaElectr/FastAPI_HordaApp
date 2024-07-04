from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select
from sqlalchemy import delete
from sqlalchemy import Result

from models import Stock

from exceptions import DataBaseConnectionError
from exceptions import PydanticDumpException

from schemas import StockCreateSchema2
from schemas import StockSchema

from exceptions import PydanticDumpException
from exceptions import DataBaseConnectionError


# StockCreateSchema2 - schema with company_id and product_id
async def create_stocks(
    session: AsyncSession,
    stocks_creates: list[StockCreateSchema2],
    ) -> list[Stock]:

    try:
        stocks = [
            Stock(**stock.model_dump())
            for stock in stocks_creates
        ]
    except Exception as e:
        print(e)
        raise PydanticDumpException()

    session.add_all(stocks)

    try:
        await session.commit()
    except Exception as e:
        raise DataBaseConnectionError()

    return stocks


async def create_stock(
    session: AsyncSession,
    create_stock: StockCreateSchema2,
    ) -> Stock:

    stock = Stock(**create_stock.model_dump())

    session.add(stock)

    try:
        await session.commit()
    except Exception as e:
        print(e)
        raise DataBaseConnectionError()

    return stock


async def get_all_stocks(
    session: AsyncSession,
    ) -> list[Stock]:

    stmt = (
        select(Stock)
        .order_by(Stock.id)
    )

    result: Result = await session.execute(stmt)
    stocks = list(result.scalars().all())

    return stocks

    
async def get_stock_by_id(
    session: AsyncSession,
    stock_id: int,
    ) -> Stock | None:

    stmt = (
        select(Stock)
        .where(Stock.id == stock_id)
    )

    result: Result = await session.execute(stmt)
    stock = result.scalar_one_or_none()

    return stock

    
async def delete_all_stocks(
    session: AsyncSession,
    ) -> None:

    stmt = delete(Stock)

    await session.execute(stmt)
    await session.commit()




    
    
    