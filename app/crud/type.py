from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select
from sqlalchemy import delete
from sqlalchemy import Result

from models import Type

from exceptions import DataBaseConnectionError
from exceptions import PydanticDumpException

from schemas import TypeCreateSchema
from schemas import TypeSchema


async def get_all_types(
    session: AsyncSession,
) -> list[Type]:

    stmt = (
        select(Type)
        .order_by(Type.id)
    )

    try: 
        result: Result = await session.execute(stmt)
    except Exception as e:
        raise DataBaseConnectionError(
            f"###error to connect db {str(e)}"
            )

    types = list(result.scalars().all())

    return types

async def create_type(
    session: AsyncSession,
    type_create: TypeCreateSchema,
) -> Type:

    try:
        type1= Type(
            **type_create.model_dump()
        )
    except Exception as e:
        raise PydanticDumpException(
            f"###pydantic error {str(e)}"
            )

    session.add(type1)

    try: 
        await session.commit()
    except Exception as e:
        raise DataBaseConnectionError(
            f"### errorr to connect db {str(e)}"
            )

    return type1
    

async def create_types(
    session: AsyncSession,
    type_creates: list[TypeCreateSchema],
    ) -> list[Type]:

    try: 
        types = [
            Type(**type1.model_dump())
            for type1 in type_creates
        ]

    except Exception as e:
        print(e)
        raise PydanticDumpException()

        
        
    session.add_all(types)
    
    try:
        await session.commit()
        
    except Exception as e:
        raise DataBaseConnectionError()
    
    return types



async def delete_all_types(
    session: AsyncSession,
    ) -> None:
    
    stmt = (
        delete(Type)
    )

    await session.execute(stmt)
    await session.commit()

    

        

