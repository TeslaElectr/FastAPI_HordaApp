import factory
from sqlalchemy.ext.asyncio import AsyncSession
from faker import Faker

from app.models import Product
from tests.factories.company import CompanyFactory
from tests.factories.type import TypeFactory


fake = Faker()

class ProductFactory(factory.alchemy.SQLAlchemyModelFactory):

    company_id = None
    type_id = None
    
    def __init__(self, company_id, type_id):
        ProductFactory.company_id = company_id
        ProductFactory.type_id = type_id

    class Meta:
        model = Product
        sqlalchemy_session_persistence = None

    id = factory.Sequence(lambda n: n)
    name = factory.LazyAttribute(lambda _: fake.word())
    description = factory.LazyAttribute(lambda obj: f"This is description of product - {obj.name}: {fake.text()}")

    company = factory.SubFactory(CompanyFactory)
    type1 = factory.SubFactory(TypeFactory)


    @factory.post_generation
    def stocks(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for stock in extracted:
                self.stocks.append(stock) # type: ignore

                
    @factory.post_generation
    def assoc_details(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for detail in extracted:
                self.assoc_details.append(detail) # type: ignore
        

    

     


    