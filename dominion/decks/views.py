from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView

from .models import Deck
from .forms import DeckFactoryForm


class DeckList(ListView):
    model = Deck
    context_object_name = 'decks'


class DeckDetail(DetailView):
    model = Deck
    context_object_name = 'deck'


class DeckFactory(FormView):
    form_class = DeckFactoryForm
    success_url = '/'
    template_name = 'form_view.html'

    def get_context_data(self, **kwargs):
        context = super(DeckFactory, self).get_context_data(**kwargs)
        context['subtitle'] = "Deck Builder"
        return context