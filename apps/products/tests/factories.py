import factory
from faker import Faker

from apps.products.models import Product

fake = Faker()


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    nombre = factory.LazyFunction(lambda: fake.word().capitalize())
    descripcion = factory.LazyFunction(lambda: fake.text(max_nb_chars=200))
    precio = factory.LazyFunction(lambda: fake.random_int(min=100, max=10000))
    disponible = True
