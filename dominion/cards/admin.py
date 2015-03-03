from django.contrib import admin
from django.conf import settings

from .models import Card, CardSet, CardType


class CardAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        if not obj.image:
            return ""

        return '<img src="{}{}" width="35">'.format(
            settings.MEDIA_URL,
            obj.image,
        )
    image_tag.allow_tags = True
    image_tag.short_description = "Card Image"

    list_display = (
        'name',
        'card_set',
        'card_type',
        'cost',
        'image_tag'
    )
    list_filter = (
        'card_set',
        'card_type',
    )
    search_fields = (
        'name',
        'card_set__name',
        'card_type__name',
    )

    actions = ['fetch_image']

    def fetch_image(self, request, queryset):
        for card in queryset:
            card.fetch_image()
    fetch_image.short_description = "Fetch card images"


admin.site.register(Card, CardAdmin)
admin.site.register(CardSet)
admin.site.register(CardType)
