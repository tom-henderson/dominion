from django import forms
from django.core.exceptions import ValidationError

from common.forms import BootStrapModelForm, BootStrapForm

from cards.models import CardSet
from .models import Deck


class DeckForm(BootStrapModelForm):
    class Meta:
        model = Deck

    def clean(self):
        cards = self.cleaned_data.get('cards')
        if cards.count() != 10:
            raise ValidationError(
                'A deck must have exactly 10 cards, not {}.'.format(cards.count())
            )
        return super(DeckForm, self).clean()


class DeckFactoryForm(BootStrapForm):
    card_sets = forms.ModelChoiceField(
        label="Card Sets",
        empty_label=None,
        widget=forms.CheckboxSelectMultiple,
        queryset=CardSet.objects.all().exclude(name="Base Cards").exclude(name="Common"),
    )
    card_price_randomness = forms.ChoiceField(
        label="Cad Prices",
        choices=(('random', 'Random'), ('even', 'Even'))
    )
