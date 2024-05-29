from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from schemas import ProductSchema
from schemas import ProductCreateSchema

from db import session_dependency

from crud import product as crud_product

from models import Product


router = APIRouter(
    prefix="/product",
    tags=["Product"],
)


@router.get("/", response_model=list[ProductSchema])
async def get_all_products(
    session: AsyncSession = Depends(session_dependency),
    ) -> list[Product]:

    products = await crud_product.get_all_products(session=session)

    return products
    
    
@router.post("/create/", response_model=ProductSchema)
async def create_product(
    company_id: int,
    type_id: int,
    product_create: ProductCreateSchema,
    session: AsyncSession = Depends(session_dependency),
    ) -> Product:

    product = await crud_product.create_product(
        session=session,
        product_create=product_create, 
        company_id=company_id,
        type_id=type_id,
    )

    return product