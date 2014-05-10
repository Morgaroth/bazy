from django.shortcuts import render, redirect
from orm_app.models import Choice, Poll, PollDetails, User
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse

def index(request):
	polls = Poll.objects.all()
	return render(request,'polls/index.html',{'polls': polls})

def createchoice(request):
	Poll.objects.get(pk=request.POST['pollid']).choice_set.create(choice=request.POST['choice'], votes=0)
	return redirect(reverse('choicesindex'))	

def createpoll(request):
	poll = Poll(question=request.POST['question'])
	poll.save()
	PollDetails(poll=poll,published=timezone.now()).save()
	return redirect(reverse('choicesindex'))	
	

def vote(request):
	choice = Choice.objects.get(pk=request.POST['choiceid'])
	choice.votes+=1
	choice.save()
	return redirect(reverse('choicesindex'))	

def usersindex(request):
	users = User.objects.all()
	return render(request,'users/index.html',{'users': users})

def createuser(request):
	user = User(name=request.POST['observerName'])
	user.save()
	return redirect(reverse('usersindex'))

def watch(request):
	poll = Poll.objects.get(pk=request.POST['pollid'])
	users = User.objects.filter(name__exact=request.POST['name'])
	if(len(users)==0):
		return HttpResponse("User not exists")
	else:
		poll.observers.add(users[0])
		return redirect(reverse('choicesindex'))