from django.db import models

# Create your models here.

class Poll(models.Model):
	question = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.question


class PollDetails(models.Model):
	published = models.DateField()
	poll = models.OneToOneField(Poll)
	
	def __unicode__(self):
		return str(self.published)

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()
	
	def __unicode__(self):
		return str(self.id) + ' ' + self.choice + ' ' + str(self.votes)
		

