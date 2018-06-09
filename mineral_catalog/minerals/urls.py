from django.conf.urls import url

from . import views

app_name = 'minerals'
urlpatterns = [
    url(r'^random/$', views.mineral_random, name='random'),
    url(r'^$', views.all_minerals, name='list'),
    url(r'^(?P<pk>\d+)/$', views.mineral_detail, name='detail'),
    url(r'^(?P<string>\D)$', views.mineral_filter, name='filter'),
    url(r'^group/(?P<group_name>\w+|\w+\s\w+)$', views.mineral_group,
        name='group'),
    url(r'^search$', views.mineral_search, name='search'),
]
