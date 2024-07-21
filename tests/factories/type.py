import factory
from faker import Faker

from app.models import Type

fake = Faker()

class TypeFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = Type
        sqlalchemy_session_persistence = None

    id = factory.Sequence(lambda n: n)
    name = factory.LazyAttribute(lambda _: fake.word())
    description = factory.LazyAttribute(lambda obj: f"This is type - {obj.name}: {fake.text()}")

    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        if not create:
            return None

        if extracted:
            for product in extracted:
                self.products.append(product) # type: ignore
    