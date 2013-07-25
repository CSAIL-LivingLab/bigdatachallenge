from django.conf.urls import patterns, url

from home import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^info$', views.info, name='info'),
  url(r'^prediction$', views.prediction, name='prediction'),
  url(r'^visualization$', views.visualization, name='visualization')
)