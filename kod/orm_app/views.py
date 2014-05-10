from django.shortcuts import render, redirect
from orm_app.models import Choice, Poll

def index(request):
	polls = Poll.objects.all()
	return render(request,'polls/index.html',{'polls': polls})

def createchoice(request):
	Poll.objects.get(pk=request.POST['pollid']).choice_set.create(choice=request.POST['choice'], votes=0)
	return index(request)	

def createpoll(request):
	Poll(question=request.POST['question']).save()
	return index(request)

def vote(request):
	choice = Choice.objects.get(pk=request.POST['choiceid'])
	choice.votes+=1
	choice.save()
	return index(request)