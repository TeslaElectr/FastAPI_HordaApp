from typing import TYPE_CHECKING
import logging
import threading
from contextlib import ExitStack
import asyncio
import pytest

from pytest_postgresql import factories
from pytest_postgresql.janitor import DatabaseJanitor

from fastapi.testclient import TestClient

from app import init_app

from app.db import sessionmanager
from app.db import get_db

from app.schemas import CompanyCreateSchema
from app.schemas import TypeCreateSchema

from app.crud import type as crud_type
from app.crud import company as crud_company

from tests.factories import CompanyFactory
from tests.factories import TypeFactory

from sqlalchemy.ext.asyncio import AsyncSession

if TYPE_CHECKING:
    from app.models import Company
    from app.models import Type




# logging settings
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@pytest.fixture(autouse=True)
def app():
    with ExitStack():
        yield init_app(init_db=False)


@pytest.fixture
def client(app):
    with TestClient(app=app) as c:
        yield c


import os

## need for use postgresql_proc() and testing_db_cruds
os.environ["PG_CTL"] = "pg_ctlcluster"
test_db = factories.postgresql_proc(port=None, dbname="test_db")


# @pytest.fixture(scope="session", autouse=True)
# def event_loop(request):
#     try:
#         loop = asyncio.get_event_loop()
#     except RuntimeError as e:
#         if str(e).startswith("There is no current event loop in thread"):
#             loop = asyncio.new_event_loop()

#             asyncio.set_event_loop(loop=loop)
#         else:
#             raise
        
#     yield loop
#     loop.close()


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
async def connection_test(test_db, event_loop):
    pg_host = test_db.host
    pg_port = test_db.port
    pg_user = test_db.user
    pg_db = test_db.dbname
    pg_password = test_db.password

    with DatabaseJanitor(
        user=pg_user,
        host=pg_host,
        port=pg_port,
        dbname=pg_db,
        version=test_db.version,
        password=pg_password,
    ):

        connection_str = f"postgresql+psycopg://{pg_user}:@{pg_host}:{pg_port}/{pg_db}"
        sessionmanager.init(host=connection_str)
        os.environ["DATABASE_URL"] = connection_str
        yield
        await sessionmanager.close()


@pytest.fixture(scope="function", autouse=True)
async def create_tables(request, connection_test):
    async with sessionmanager.connect() as connection:
        if "test_alembic_migrations" not in request.keywords:
            await sessionmanager.drop_all(connection=connection)
            await sessionmanager.create_all(connection=connection)
        else:
            await sessionmanager.drop_all(connection=connection)


@pytest.fixture(scope="function", autouse=True)
async def session_override(app, connection_test):
    async def get_test_db():
        async with sessionmanager.session() as session:
            yield session

    app.dependency_overrides[get_db] = get_test_db


@pytest.fixture
async def session(connection_test):
    async with sessionmanager.session() as session:
        logger.debug(f"This is fuxture session - {threading.current_thread().name}")
        yield session

        
@pytest.fixture
def create_companies():
    async def _create_companies(num_of_companise_create: int, session: AsyncSession):

        number_of_factories = 0
        
        while number_of_factories < num_of_companise_create:
            company_data_all = CompanyFactory.build()
            company_data_create = {k: v for k, v in company_data_all.__dict__.items() if not k.startswith("_")}
            company_create = CompanyCreateSchema(**company_data_create)
            number_of_factories += 1
            await crud_company.create_company(session=session, company_create=company_create)

        companies: list[Company] = await crud_company.get_all_companies(session=session)
        return companies

    return _create_companies

    
    
@pytest.fixture
def create_typies():
    async def _create_typies(num_of_typies_create: int, session: AsyncSession):

        number_of_factories = 0

        while number_of_factories < num_of_typies_create:
            type_data_all = TypeFactory.build()
            type_data_create = {k: v for k, v in type_data_all.__dict__.items() if not k.startswith("_")}
            type_create = TypeCreateSchema(**type_data_create)
            number_of_factories += 1
            await crud_type.create_type(session=session, type_create=type_create)

        typies: list[Type] = await crud_type.get_all_types(session=session)
        return typies
    
    return _create_typies

