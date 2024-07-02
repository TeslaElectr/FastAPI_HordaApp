import time
import subprocess
import logging
import asyncio
import pytest

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from alembic.config import Config
from alembic import command

from app.models import Base

from tests.factories import CompanyFactory
from .core import settings


# logging settings
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def event_loop():
    logger.debug("Setting up event loop fixture. ")
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()
    logger.debug("Event loop fixture finished. ")

    
@pytest.fixture(scope="session")
def docker_compose_up():
    logger.debug("Starting docker. ")
    subprocess.run(["docker-compose", "up", "-d", "pg_test"])
    time.sleep(10)
    yield
    subprocess.run(["docker-compose", "down"])
    logging.debug("docker stoped. ")


@pytest.fixture(scope="session")
async def engine():
    logger.debug("Create async engine. ")
    async_engine = create_async_engine(url=settings.DB_URL)
    yield async_engine
    await async_engine.dispose()
    logger.debug("Async engine dispose. ")


@pytest.fixture(scope="session")
async def apply_migrations(engine):
    logger.debug("Applying migrations. ")

    alembic_cfg = Config("alembic.ini")
    alembic_cfg.attributes["configure_logger"] = False
    command.upgrade(alembic_cfg, "head")
    yield
    command.downgrade(alembic_cfg, "head")
    logger.debug("Migration rolled back. ")
    

@pytest.fixture(scope="function")
async def async_session(engine):
    logger.debug("Create async session. ")
    async_session = async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=settings.expire_on_commit
        )
    async with async_session() as session:
        yield session

    await session.rollback()
    logger.debug("Async session finished. ")

        
        
# @pytest.fixture(scope="function")
# def setup_factories(async_session):
#     CompanyFactory._meta.sqlal
    
