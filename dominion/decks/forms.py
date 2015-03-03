from django import forms
from django.core.exceptions import ValidationError

from common.forms import BootStrapModelForm, BootStrapForm

from cards.models import CardSet
from .models import Deck, deck_factory


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
    name = forms.CharField(max_length=30)
    card_sets = forms.ModelMultipleChoiceField(
        label="Card Sets",
        widget=forms.CheckboxSelectMultiple,
        queryset=CardSet.objects.all().exclude(name="Base Cards").exclude(name="Common"),
    )
    # card_price_randomness = forms.ChoiceField(
    #     label="Cad Prices",
    #     choices=(('random', 'Random'), ('even', 'Even'))
    # )

    def is_valid(self):
        super(DeckFactoryForm, self).is_valid()

        name = self.cleaned_data['name']
        card_sets = self.cleaned_data['card_sets']

        print card_sets
        print name

        deck = deck_factory(
            name=name,
            card_sets=CardSet.objects.filter(id__in=card_sets)
        )

        return True
