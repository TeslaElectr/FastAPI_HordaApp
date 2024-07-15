import logging
from contextlib import ExitStack
import asyncio
import pytest

from pytest_postgresql import factories
from pytest_postgresql.janitor import DatabaseJanitor

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi.testclient import TestClient

from alembic.config import Config
from alembic import command

from app import init_app
from app.db import sessionmanager
from app.db import get_db
from app.models import Base

from tests.factories import CompanyFactory
from tests.core import settings


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


@pytest.fixture(scope="session")
def event_loop(request):
    try:
        loop = asyncio.get_event_loop_policy().get_event_loop()
    except RuntimeError as e:
        if str(e).startswith('There is no current event loop in thread'):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop=loop)
        else:
            raise
        
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


## ALEMBIC MIGRATION FIXTURE. error with 2 tests "RuntimeError There is no current event loop in thread 'MainThread'"
# @pytest.fixture(scope="function", autouse=True)
# def alembic_upgrade_downgrade(event_loop, connection_test):
#     with sessionmanager.alembic_run_migrations():
#         yield


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
        yield session
