from django.db import models

# Create your models here.

		
class Poll(models.Model):
	question = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.question

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()
	
	def __unicode__(self):
		return str(self.id) + ' ' + self.choice + ' ' + str(self.votes)
		

