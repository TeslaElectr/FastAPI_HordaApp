from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from db import get_db
# from db import db_conn as db_helper

# from models import Production

# from schemas import ProductionCreateSchema
# from schemas import ProductionSchema

from crud import production as crud_production

router = APIRouter(
    prefix="/productions",
    tags=["Production"],
)


# @router.post("/", response_model=ProductionSchema)
# async def add_production(
#     product_id: int,
#     create_production: ProductionCreateSchema,
#     session: AsyncSession = Depends(get_db),
#     ) -> Production:
    
#     production = await crud_production.create_production(
#         session=session,
#         production_create=create_production,
#         product_id=product_id,
#     )

#     return production
    
    