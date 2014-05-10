from django_faker import Faker
populator = Faker.getPopulator()

from orm_app.models import Choice, Poll

populator.addEntity(Poll, 1, {
	'question': lambda x: populator.generator.sentenc()		
})

populator.addEntity(Choice, 3, {
    'choice':    lambda x: populator.generator.sentence(),
    'votes': lambda x: populator.generator.randomInt(0,25),
})
populator.execute()

insertedPks = populator.execute()
