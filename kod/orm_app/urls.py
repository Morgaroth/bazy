from django.conf.urls import patterns, url

from orm_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='choicesindex'),
    url(r'^newpoll$', views.createpoll, name='createpoll'),
    url(r'^newchoice$', views.createchoice, name='createchoice'),
    url(r'^vote$', views.vote, name='vote'),
)