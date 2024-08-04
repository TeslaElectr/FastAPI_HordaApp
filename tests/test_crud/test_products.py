import logging
from typing import TYPE_CHECKING

import random
import threading

import asyncio
import pytest

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.product import get_all_products
from app.crud.product import create_product
from app.schemas import ProductCreateSchema

from tests.factories import ProductFactory

if TYPE_CHECKING:
    from app.models.product import Product


# logging settings
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@pytest.mark.asyncio(scope="session")
async def test_create_products(session: AsyncSession, create_companies, create_typies):
    num_of_typies = 4
    num_of_companies = 20
    num_of_products = num_of_companies * 4

    
    logger.debug(f"This is test_create_products  - {threading.current_thread().name}")

    await create_companies(
        num_of_companise_create=num_of_companies,
        session=session,
        )
    await create_typies(
        num_of_typies_create=num_of_typies,
        session=session
        )

    for i in range(num_of_products):
        company_id = random.randint(1, num_of_companies)
        type_id = random.randint(1, num_of_typies)

        product_data_all = ProductFactory.build()

        product_data_create = {k: v for k, v in product_data_all.__dict__.items() if not k.startswith("_")}
        product_data_create["name"] = f"{product_data_create["name"]}_{i}"
        product_create = ProductCreateSchema(**product_data_create)

        await create_product(
            session=session,
            product_create=product_create,
            company_id=company_id,
            type_id=type_id,
            ) 

        

    products: list[Product] = await get_all_products(session=session)

    logger.debug(f"This is {threading.current_thread().name}")

    assert len(products) == num_of_products


@pytest.mark.test_event_loop
@pytest.mark.asyncio
async def test_runs_in_a_loop():
    assert asyncio.get_running_loop()


# @pytest.mark.asyncio
# async def test_add_company(session: AsyncSession):

#     number_of_factories = 0
#     company_list = []

#     logger.debug(f"This is test_add_company - {threading.current_thread().name}")

#     while number_of_factories < 20:
#         company_data_all = CompanyFactory.build()
#         company_data_create = {
#             k: v for k, v in company_data_all.__dict__.items() if not k.startswith("_")
#         }
#         company_create = CompanyCreateSchema(**company_data_create)
#         number_of_factories += 1
#         await create_company(session=session, company_create=company_create)

#     companies: list[Company] = await get_all_companies(session=session)

#     assert len(companies) == number_of_factories