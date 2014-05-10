from django_faker import Faker
populator = Faker.getPopulator()

from orm_app.models import Choice

populator.addEntity(Choice, 100, {
    'choice':    lambda x: populator.generator.sentence(),
    'votes': lambda x: populator.generator.randomInt(0,25),
})
populator.execute()

insertedPks = populator.execute()
