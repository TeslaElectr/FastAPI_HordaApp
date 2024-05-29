from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from schemas import TypeSchema
from schemas import TypeCreateSchema

from db import db_conn as db_helper

from crud import type as crud_type

from models import Type


router = APIRouter(
    prefix="/types",
    tags=["Type"],
)


@router.get("/", response_model=list[TypeSchema])
async def get_all_types(
    session: AsyncSession = Depends(db_helper.session_dependency),
    ) -> list[Type]:

    types = await crud_type.get_all_types(session=session)

    return types
    
    
@router.post("/create/", response_model=TypeSchema)
async def create_type(
    type_create: TypeCreateSchema,
    session: AsyncSession = Depends(db_helper.session_dependency),
    ) -> Type:

    type1 = await crud_type.create_type(
        session=session,
        type_create=type_create, 
    )

    return type1