from django.conf.urls import patterns, url

from orm_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^users$', views.usersindex, name='usersindex'),
    url(r'^newpoll$', views.createpoll, name='createpoll'),
    url(r'^newchoice$', views.createchoice, name='createchoice'),
    url(r'^createuser$', views.createuser, name='createuser'),
    url(r'^vote$', views.vote, name='vote'),
    url(r'^watch$', views.watch, name='watch'),
)