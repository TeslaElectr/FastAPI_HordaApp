import asyncio

from models import Product
from models import Company
from models import Stock
from models import Type
from models import Production
from models import Recipe

from crud import company as crud_company

from db import db_conn as db_helper


async def main():
    async with db_helper.create_session() as session:
        pass


if __name__ == "__main__":
    asyncio.run(main())




