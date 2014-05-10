from django.db import models

# Create your models here.

class Poll(models.Model):
	question = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.question

class Choice(models.Model):
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()
	#poll = models.ForeignKey(Poll,)
	
	def __unicode__(self):
		return str(self.id) + ' ' + self.choice + ' ' + str(self.votes)
		

