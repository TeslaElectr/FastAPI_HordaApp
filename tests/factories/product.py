
import factory
from sqlalchemy.ext.asyncio import AsyncSession
from faker import Faker

from app.models import Product


fake = Faker()

class ProductFactory(factory.alchemy.SQLAlchemyModelFactory):
    
    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n)
    description = factory.LazyAttribute(lambda _: fake.text())
     
    ...


    