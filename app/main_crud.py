import asyncio

from sqlalchemy.ext.asyncio import AsyncSession

from models import Product
from models import Company
from models import Stock
from models import Type
from models import Production
from models import Recipe

from crud import company as crud_company
from crud import product as crud_product

from schemas import CompanyCreateSchema
from schemas import ProductCreateSchema
from schemas import ProductionCreateSchema

from db import db_conn as db_helper

from tests.cfg_company import get_list_companies
    

async def create_companies(
    session: AsyncSession,
    ):

    create_companies = get_list_companies()

    result = await crud_company.create_companies(
        session=session,
        company_list=create_companies,
        )
    return result


async def create_products(
    session: AsyncSession,
    ):

    products_list = ...

    result = await crud_product.create_products(
        session=session,
       create_products=products_list,
        )

    return result


async def main():
    async with db_helper.session_factory() as session:
        company_list = await create_companies(session=session)
        print(company_list)


if __name__ == "__main__":
    asyncio.run(main())




