import pytest

from sqlalchemy import Result
from sqlalchemy import text

from app.models import Company
from app.crud.company import get_all_companies
from app.crud.company import create_company
from app.crud.company import create_companies
from app.crud.company import delete_all_companies

from app.schemas import CompanyCreateSchema

from tests.factories import CompanyFactory
from tests.conftest import logger


@pytest.mark.asyncio
async def test_add_company(session):

    number_of_factories = 0
    company_list = []
    
    while number_of_factories < 20:
        company_data_all = CompanyFactory.build()
        company_data_create = {k: v for k, v in company_data_all.__dict__.items() if not k.startswith("_")}
        company_create = CompanyCreateSchema(**company_data_create)
        number_of_factories += 1
        await create_company(session=session, company_create=company_create)

    companies: list[Company] = await get_all_companies(session=session)

    assert len(companies) == number_of_factories

    
@pytest.mark.asyncio
async def test_add_companies(session):

    number_of_factories = 0
    company_list = []

    while number_of_factories < 20:
        company_data_all = CompanyFactory.build()
        company_data_create = {k: v for k, v in company_data_all.__dict__.items() if not k.startswith("_")}
        company_list.append(CompanyCreateSchema(**company_data_create))
        number_of_factories += 1

    await create_companies(session=session, company_list=company_list)
    companies: list[Company] = await get_all_companies(session=session)

    assert len(companies) == number_of_factories

    


def test_get_companies(client):
    response = client.get("/companies")
    assert response.status_code == 200
    assert response.json() == []

    
