from django.conf.urls import patterns, include, url

from .views import DeckList, DeckDetail

urlpatterns = patterns('',
    url(r'^$', DeckList.as_view(), name='deck_list'),
    url(r'^(?P<pk>\d+)/$', DeckDetail.as_view(), name='deck_detail'),
)
