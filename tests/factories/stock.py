import pytest
import factory
from faker import Faker

fake = Faker()

from app.models import Stock
from tests.factories.company import CompanyFactory
from tests.factories.product import ProductFactory

class StockFactory(factory.alchemy.SQLAlchemyModelFactory):

    company_id = None
    product_id = None

    def __init__(self, company_id, product_id):
        StockFactory.company_id = company_id
        StockFactory.product_id = product_id
    
    class Meta:
        model = Stock
        sqlalchemy_session_persistence = None

        
    id = factory.Sequence(lambda n: n)
    name = factory.LazyAttribute(lambda _: fake.word())
    # weight = factory.LazyAttribute(lambda _: )
    description = factory.LazyAttribute(lambda obj: f"This is stock description stock.name = {obj.name}: {fake.text()}")

    company = factory.SubFactory(CompanyFactory)
    product = factory.SubFactory(ProductFactory)

    
    @factory.post_generation
    def assoc_details(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for detail in extracted:
                self.assoc_details.append(detail) #type: ignore

    