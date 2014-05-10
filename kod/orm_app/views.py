from django.shortcuts import render, redirect
from orm_app.models import Choice, Poll, PollDetails
from django.utils import timezone

def index(request):
	polls = Poll.objects.all()
	print polls[0]
	return render(request,'polls/index.html',{'polls': polls})

def createchoice(request):
	Poll.objects.get(pk=request.POST['pollid']).choice_set.create(choice=request.POST['choice'], votes=0)
	return index(request)	

def createpoll(request):
	poll = Poll(question=request.POST['question'])
	poll.save()
	PollDetails(poll=poll,published=timezone.now()).save()
	return index(request)

def vote(request):
	choice = Choice.objects.get(pk=request.POST['choiceid'])
	choice.votes+=1
	choice.save()
	return index(request)