from django.shortcuts import render, redirect
from orm_app.models import Choice

def index(request):
	choices = Choice.objects.all()
	return render(request,'choices/index.html',{'choices': choices})

def createpage(request):
	return render(request,'choices/create.html')

def created(request):
	Choice(choice=request.POST['choice'], votes=request.POST['votes']).save()
	return index(request)

def vote(request):
	choice = Choice.objects.get(pk=request.POST['choiceid'])
	choice.votes+=1
	choice.save()
	return index(request)