from typing import TYPE_CHECKING

import random

import asyncio

import pytest

from app.crud.product import get_all_products
from app.crud.product import get_proudct_by_id
from app.crud.product import create_product
from app.crud.product import create_products

from app.crud.product import delete_all_products

from tests.factories import ProductFactory

if TYPE_CHECKING:
    from app.models.product import Product


@pytest.mark.asyncio
async def test_create_products(event_loop, session, create_companies, create_typies):
    async def run_test(session, create_companies, create_typies):

        num_of_typies = 4
        num_of_companies = 20
        num_of_products = num_of_companies * 4

        companies = await create_companies(
            num_of_companise_create=num_of_companies, session=session
        )
        typies = await create_typies(num_of_typies_create=num_of_typies, session=session)

        for _ in range(num_of_products):
            company_id = random.randint(1, num_of_companies)
            type_id = random.randint(1, num_of_typies)

            product_data_all = ProductFactory(
                company_id=company_id,
                type_id=type_id,
            )

        products: list[Product] = await get_all_products(session=session)

        assert len(products) == num_of_products
    

    await event_loop.run_until_complete(
        run_test(
            session=session,
            create_companies=create_companies,
            create_typies=create_typies,
            )
        )
