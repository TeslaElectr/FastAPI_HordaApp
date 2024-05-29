import asyncio

from sqlalchemy.ext.asyncio import AsyncSession

from models import Product
from models import Company
from models import Stock
from models import Type
from models import Production
from models import Recipe

from crud import company as crud_company
from schemas import CompanyCreateSchema

from db import db_conn as db_helper

def get_list_companies():
    horda = CompanyCreateSchema(
        name="Horda",
        city="Saint-Petersburg",
        inn=7813299598,
        kpp=781301001,
        address="197022, gorod Sankt-Peterburg, ul CHapygina, d. 6 litera P, ofis 214, r.m. 1",
        phone=79999999999,
        email="ivan_lo@hordanpp.com"
    )

    amdor = CompanyCreateSchema(
        name="Amdor",
        city="N-Tagil",
        inn=6623024667,
        kpp=662301001,
        address="622051, Sverdlovskaya oblast', gorod Nizhnij Tagil, Severnoe sh., d.21",
        phone=75555555555,
        email="amdor@ucp.ru",
    )

    return [horda,amdor]

    
async def create_companies(
    session: AsyncSession,
    create_companies: CompanyCreateSchema,
    ):

    create_companies = get_list_companies()

    result = await crud_company.create_companies(
        session=session,
        company_list=create_companies,
        )
    return result

async def main():
    async with db_helper.session_factory() as session:
        companies = get_list_companies()
        company_list = await create_companies(session=session, create_companies=companies)
        print(company_list)


if __name__ == "__main__":
    asyncio.run(main())




