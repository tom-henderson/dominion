from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import Http404

from .models import Card, CardSet


class CardList(ListView):
    model = Card
    context_object_name = 'cards'


class CardDetail(DetailView):
    model = Card

    # TODO: Should really be using slug fields here.
    def get_object(self):
        if self.kwargs.get('card_set', None) and self.kwargs.get('card_name', None):
            return get_object_or_404(
                Card,
                card_set=CardSet.objects.get(name=self.kwargs['card_set']),
                name=self.kwargs['card_name']
            )
        elif self.kwargs.get('pk', None):
            return get_object_or_404(Card, id=self.kwargs['pk'])
        else:
            raise Http404
