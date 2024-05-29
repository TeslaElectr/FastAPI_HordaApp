from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import async_sessionmaker

from core import config

class DataBaseHelper:

    def __init__(
        self,
        url: str = config.DB_URL,
        echo: bool = config.DB_ECHO,
        max_overflow: int = config.DB_max_overflow,
        pool_size: int = config.DB_pool_size,
        ):

        self.url = url
        self.echo = echo
        self.max_overflow = max_overflow
        self.pool_size = config.DB_pool_size

        self.engine = create_async_engine(
            url=self.url,
            echo=self.echo,
            max_overflow=self.maxoverflow,
            pool_size=self.pool_size,
        )

        self.session_factory = async_sessionmaker(
            
            bind=self.engine,
            class_=AsyncSession,
            autoflush=False,
            expire_on_commit=False,
        )


    async def session_dependency(self):
        self.session = self.session_factory
        async with self.session as conn:
            yield conn


db_conn = DataBaseHelper()
