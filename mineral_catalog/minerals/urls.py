from django.conf.urls import url

from . import views

app_name = 'minerals'
urlpatterns = [
    url(r'random/$', views.mineral_random, name='random'),
    url(r'^$', views.mineral_list, name='list'),
    url(r'(?P<pk>\d+)/$', views.mineral_detail, name='detail'),
]