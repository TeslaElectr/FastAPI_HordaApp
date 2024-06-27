from sqlalchemy.ext.asyncio import AsyncSession
from faker import Faker

from app.models import Company

import factory


fake = Faker()


class CompanyFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Company
        
    id = factory.Sequence(lambda n: n)
    name = factory.LazyAttribute(lambda _: fake.company())
    city = factory.LazyAttribute(lambda _: fake.city())
    inn = factory.Sequence(lambda n: 10000000000 + n)
    kpp = factory.Sequence(lambda n: 20000000000 + n)
    address = factory.LazyAttribute(lambda _: fake.address())
    phone = factory.Sequence(lambda n: 70000000000 + n)
    email = factory.LazyAttribute(lambda _: fake.email())

    
    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for product in extracted:
                self.products.append(product) # type: ignore

                
                
    @factory.post_generation
    def stocks(self, create, extracted, **kwargs):
        if not create:
            return 
        
        if extracted:
            for stock in extracted:
                self.stocks.append(stock) # type: ignore

                
                
    @factory.post_generation
    def warehouses(self, create, extracted, **kwargs):
        if not create:
            return
        
        if extracted:
            for warehouse in extracted:
                self.warehouses.append(warehouse) # type: ignore
                
    
    



