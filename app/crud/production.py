# from sqlalchemy.ext.asyncio import AsyncSession

# from schemas import ProductionSchema
# from schemas import ProductionCreateSchema

# from exceptions import DataBaseConnectionError

# from models import Production

# from . import product as crud_product



# async def create_production(
#     session: AsyncSession,
#     production_create: ProductionCreateSchema,
#     product_id: int,
    
#     ) -> Production:
    
#     production = Production(
#         **production_create,
#     )

#     product = crud_product.get_proudct_by_id(
#         session=session,
#         product_id=product_id,
#         )

#     #add services func for add stocks of production
#     #this info we can get from receptyre file which we need create.
    
#     production.products.append(product)
#     # production.stocks_m2m.extend(stocks)

#     # add products and stocks here for m2m relationship

#     session.add(production)

#     try:
#         await session.commit()
#     except Exception as e:
#         print (e)
#         raise DataBaseConnectionError()

#     return production
        
        