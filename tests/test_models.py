import pytest

from tests.factories import CompanyFactory
from sqlalchemy import Result
from sqlalchemy import text

from app.models import Company


@pytest.mark.asyncio
async def test_add_companies(session):

    company_data_all = CompanyFactory.build()
    company_data_create = {k: v for k, v in company_data_all.__dict__.items() if not k.startswith("_")}
    company1 = Company(**company_data_create)

    session.add(company1)

    await session.commit()

    result: Result = await session.execute("SELECT COUNT(*) FROM companys")
    count = result.scalar_one()

    assert count == 1


@pytest.mark.asyncio
async def test_example(async_session):

        result = await async_session.execute(text("SELECT 1"))
        assert result.scalar() == 1


    

    