from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import CompanySchema
from app.schemas import CompanyCreateSchema

# from db import db_conn as db_helper
from app.db import get_db

from app.crud import company as crud_company

from app.models import Company


router = APIRouter(
    prefix="/companies",
    tags=["Company"],
)


@router.get("/", response_model=list[CompanySchema])
async def show_all_companies(
    session: AsyncSession = Depends(get_db)
    ) -> list[Company]:

    companies = await crud_company.get_all_companies(session=session)
        
    return companies

    
@router.post("/", response_model=CompanySchema)
async def add_company(
    company_add: CompanyCreateSchema,
    session: AsyncSession = Depends(get_db),
    ) -> Company:

    company = await crud_company.create_company(
        session=session,
        company_create=company_add,
        )

    return company