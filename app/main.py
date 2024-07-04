import contextlib

from fastapi import FastAPI


from db.database import sessionmanager
from core import settings




def init_app(init_db=True) -> FastAPI:

    if init_db:
        sessionmanager.init(settings.DB_URL)

        @contextlib.asynccontextmanager
        async def lifespan(app: FastAPI):
            yield
            if sessionmanager._engine is not None:
                await sessionmanager.close()

    application = FastAPI(lifespan=lifespan)

    from api.v1.endpoints import companies
    from api.v1.endpoints import products
    from api.v1.endpoints import types

    application.include_router(companies.router)
    application.include_router(products.router)
    application.include_router(types.router)

    @application.get("/")
    async def HelloWorld():
        return {"Hello":"World!"}

    return application

app = init_app()
    
    
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=8001,
        reload=True,
    )