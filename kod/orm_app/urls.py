from django.conf.urls import patterns, url

from orm_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='choicesindex'),
    url(r'^new$', views.createpage, name='createpage'),
    url(r'^create$', views.created, name='create'),
    url(r'^vote$', views.vote, name='vote'),
)