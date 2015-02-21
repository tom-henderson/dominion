from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Card


class CardList(ListView):
    model = Card
    context_object_name = 'cards'


class CardDetail(DetailView):
    model = Card
