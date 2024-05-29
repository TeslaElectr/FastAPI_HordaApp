from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Company
from schemas import CompanyCreateSchema

from exceptions import DataBaseConnectionError
from exceptions import PydanticDumpException




async def get_all_companies(
    session: AsyncSession,
) -> list[Company]:
    
    stmt = (
        select(Company)
        .order_by(Company.id)
        )

    result: Result = await session.execute(stmt)
    companies = list(result.scalars().all())
    return companies


async def create_company(
    session: AsyncSession,
    company_create: CompanyCreateSchema,
    ) -> Company:

    try:
        company = Company(**company_create.model_dump())
        
    except Exception as e:
        raise PydanticDumpException(
            f"error with .mode_dump pydantic {e.errors()}"
            )

    session.add(company)

    try:
        await session.commit()
    except Exception as e:
        raise DataBaseConnectionError(
            f"error with commit company {e.errors()}"
            )
        

    return company