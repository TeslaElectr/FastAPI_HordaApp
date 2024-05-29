from sqlalchemy.ext.asyncio import AsyncSession

from schemas import ProductionSchema
from schemas import ProductionCreateSchema

from exceptions import DataBaseConnectionError

from models import Production



async def create_production(
    session: AsyncSession,
    production_create: ProductionCreateSchema,
    
    ) -> Production:
    
    production = Production(
        **production_create,
    )

    # add products and stocks here for m2m relationship

    session.add(production)

    try:
        await session.commit()
    except Exception as e:
        print (e)
        raise DataBaseConnectionError()

    return production
        
        