import asyncio
import pytest

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from alembic.config import Config
from alembic import command

from app.models import Base
from .core import settings



@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def engine():
        async_engine = create_async_engine(url=settings.DB_URL)
        yield async_engine
        await async_engine.dispose()


@pytest.fixture(scope="session")
async def apply_migrations(engine):

    alembic_cfg = Config("alembic.ini")
    alembic_cfg.attributes["configure_logger"] = False
    command.upgrade(alembic_cfg, "head")
    yield
    command.downgrade(alembic_cfg, "head")
    

@pytest.fixture(scope="function")
async def async_session(engine):
    async_session = async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=settings.expire_on_commit
        )
    async with async_session() as session:
        yield session
        await session.rollback()
