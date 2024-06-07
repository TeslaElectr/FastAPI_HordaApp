from fastapi import FastAPI

import uvicorn

from api.v1.endpoints import companies
from api.v1.endpoints import products
from api.v1.endpoints import types

app = FastAPI()

app.include_router(companies.router)
app.include_router(products.router)
app.include_router(types.router)

@app.get("/")
async def HelloWorld():
    return {"Hello":"World!"}

    
    
if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=8001,
        reload=True,
    )