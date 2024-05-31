import pytest
import asyncio

from httpx import AsyncClient

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from app.schemas import CompanyCreateSchema
from app.db import db_conn as db_helper
from app.models import Base
from app.main import app

from session import test_db
from cfg_company import get_list_companies

async def engine_begin():
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base)

app.dependency_overrides[db_helper.session_dependency] = test_db.session_dependency


@pytest.fixture(scope="module")
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.mark.asyncio
async def test_create_companies(client):
    company_data_test: list[CompanyCreateSchema] = get_list_companies()
    for company in company-company_data_test:
        responce = await client.post("/companies/", json=company.json())
        assert responce.status_code == 200