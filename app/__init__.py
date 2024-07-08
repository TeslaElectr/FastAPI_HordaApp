import contextlib

from fastapi import FastAPI


from app.db.database import sessionmanager 
from app.core import settings


from typing import AsyncGenerator, Optional, Callable



def init_app(init_db=True) -> FastAPI:

    lifespan_context = None

    if init_db:
        sessionmanager.init(settings.DB_URL)

        @contextlib.asynccontextmanager
        async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
            yield
            if sessionmanager._engine is not None:
                await sessionmanager.close()

        lifespan_context = lifespan

    application = FastAPI(lifespan=lifespan_context)

    from app.api.v1.endpoints import companies
    from app.api.v1.endpoints import products
    from app.api.v1.endpoints import types

    application.include_router(companies.router)
    application.include_router(products.router)
    application.include_router(types.router)

    @application.get("/")
    async def HelloWorld():
        return {"Hello":"World!"}

    return application