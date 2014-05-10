from django_faker import Faker
populator = Faker.getPopulator()

from orm_app.models import Choice, Poll

#populator.addEntity(Poll, 25)

populator.addEntity(Choice, 100, {
    'choice':    lambda x: populator.generator.sentence(),
    'votes': 	lambda x: populator.generator.randomInt(0,25),
    'poll':	lambda x: Poll.objects.all()[populator.generator.randomInt(1,50)],
})

insertedPks = populator.execute()
