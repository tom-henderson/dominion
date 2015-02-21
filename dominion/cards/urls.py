from django.conf.urls import patterns, include, url

from .views import CardList, CardDetail

urlpatterns = patterns('',
    url(r'^$', CardList.as_view(), name='card_list'),
    url(r'^(?P<pk>\d+)/$', CardDetail.as_view(), name='card_detail'),
)
