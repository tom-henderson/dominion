from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

from .models import Deck
from .forms import DeckForm


class DeckAdmin(admin.ModelAdmin):
    form = DeckForm
    formfield_overrides = {
        models.ManyToManyField: {
            'widget': CheckboxSelectMultiple
        },
    }

    def card_sets(self, obj):
        return ", ".join(obj.required_card_sets)

    list_display = (
        'name',
        'card_sets',
    )


admin.site.register(Deck, DeckAdmin)