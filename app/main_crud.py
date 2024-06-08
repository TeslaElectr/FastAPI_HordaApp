import asyncio

from sqlalchemy.ext.asyncio import AsyncSession

from models import Company

from crud import company as crud_company
from crud import product as crud_product
from crud import type as crud_type

from schemas import CompanyCreateSchema
from schemas import ProductCreateSchema2
from schemas import TypeCreateSchema
from schemas import StockCreateSchema2

from db import db_conn as db_helper

from cfg_company import get_list_companies
from cfg_products import get_products_data
from cfg_type import get_type_data
    

async def create_companies(session: AsyncSession):

    create_companies: list[CompanyCreateSchema] = get_list_companies()

    result: list[Company] = await crud_company.create_companies(
        session=session,
        company_list=create_companies,
        )
    return result


async def create_products(session: AsyncSession):

    products_list: list[ProductCreateSchema2] = get_products_data()

    result = await crud_product.create_products(
       session=session,
       create_products=products_list,
        )

    return result


async def create_types(session: AsyncSession):
    type_list: list[TypeCreateSchema] = get_type_data()

    result = await crud_type.create_types(
        session=session,
        type_creates=type_list
        )

    return result

    
async def create_stocks(session: AsyncSession):
    stock_list = list[StockCreateSchema2] = ...
    


async def queries():
    async with db_helper.session_factory() as session:

        company_list = await create_companies(session=session)
        type_list = await create_types(session=session)
        print(company_list,"\n",type_list)

        product_list = await create_products(session=session)
        print(product_list)


        # await crud_product.delete_all_products(session=session)
        # await crud_company.delete_all_companies(session=session)
        # await crud_type.delete_all_types(session=session)
    

async def main():
    await queries()



if __name__ == "__main__":
    asyncio.run(main())




