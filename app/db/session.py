from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker

from core import config


engine = create_async_engine(
    url=config.DB_URL,
    echo=config.DB_ECHO,
    max_overflow=config.DB_max_overflow,
    pool_size=config.DB_pool_size,
)


async_session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    expire_on_commit=False,
)


async def session_dependency():
    async with async_session() as session:
        yield session
