import contextlib
from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from app.models import Base



class DatabaseSessionManager:
    
    def __init__(self):
        self._engine: AsyncEngine | None = None
        self._sessionmaker: async_sessionmaker | None = None
        
    def init(self, host):
        self._engine = create_async_engine(host)
        self._sessionmaker = async_sessionmaker(autocommit=False, bind=self._engine)

        
    async def close(self):
        if self._engine is None:
            raise Exception("DatabaseSessionManager is nor initialized")

        await self._engine.dispose()
        self._engine = None
        self._sessionmaker = None
    
    
    @contextlib.asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        if self._engine is None:
            raise Exception("DatabaseSessionManager is nor initialized")

        async with self._engine.begin() as connection: 
            try: 
                yield connection
            except Exception:
                await connection.rollback()
                raise

            
    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        if self._sessionmaker is None:
            raise Exception("DatabaseSessionManager is not initialized")

        session = self._sessionmaker()
        
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

            
    async def create_all(self, connection: AsyncConnection):
        await connection.run_sync(Base.metadata.create_all)


    async def drop_all(self, connection: AsyncConnection):
        await connection.run_sync(Base.metadata.drop_all)
            

sessionmanager = DatabaseSessionManager()


async def get_db():
    async with sessionmanager.session() as session:
        yield session 



