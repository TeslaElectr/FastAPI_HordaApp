from sqlalchemy import select
from sqlalchemy import delete
from sqlalchemy import Result
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Company

from app.schemas import CompanyCreateSchema
from app.schemas import CompanySchema

from app.exceptions import DataBaseConnectionError
from app.exceptions import PydanticDumpException




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
            f"error with .mode_dump pydantic {e.errors()}" # type: ignore
            )

    session.add(company)

    try:
        await session.commit()
    except Exception as e:
        raise DataBaseConnectionError(
            f"error with commit company {e.errors()}"# type: ignore
            )
        

    return company

    
    
    
async def create_companies(
    session: AsyncSession,
    company_list: list[CompanyCreateSchema],
    ) -> list[Company]:
    
    try:
        companies = [
            Company(**company.model_dump())
            for company in company_list
        ]
    except Exception as e:
        print(e)
        raise PydanticDumpException()

    session.add_all(companies)

    # try:
    await session.commit() 
    # except Exception as e:
    #     print(e)
    #     raise DataBaseConnectionError()

    return companies

    
async def delete_all_companies(
    session: AsyncSession,
    ) -> None:
    
    stmt = (
        delete(Company)
    )

    await session.execute(stmt)
    await session.commit()

    

        

