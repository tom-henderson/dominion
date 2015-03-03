import random
import datetime

from django.db import models

from cards.models import Card, CardSet

DECK_SIZE = 10


class Deck(models.Model):
    name = models.CharField(max_length=30)
    cards = models.ManyToManyField(Card)

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return "{}: [{}]".format(
            self.name,
            " / ".join(card.name for card in self.cards.all())
        )

    @property
    def required_card_sets(self):
        return set([card.card_set.name for card in self.cards.all()])


def deck_factory(name=None, card_sets=None):
    if not card_sets:
        card_sets = CardSet.objects.all()

    card_sets = card_sets.exclude(name="Base Cards").exclude(name="Common")

    if not name:
        name = "New Deck {}".format(
            datetime.datetime.now().strftime("%x")
        )

    deck = Deck()
    deck.name = name
    deck.save()

    cards = random.sample(Card.objects.filter(card_set__in=card_sets), 10)
    for card in cards:
        deck.cards.add(card)

    return deck
