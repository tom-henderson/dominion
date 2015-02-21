from datetime import datetime
from pprint import pprint

from bs4 import BeautifulSoup as bs
import requests

from django.core.management.base import BaseCommand, CommandError, NoArgsCommand

from cards.models import Card, CardSet, CardType


def strip_tags(value):
    """Returns the given HTML with all tags stripped."""
    return ''.join(bs(value).findAll(text=True))


class Command(NoArgsCommand):
    def log_message(self, message):
        self.stdout.write(
            "[{}] {}".format(
                datetime.now(),
                message,
            )
        )

    def handle_noargs(self, **options):
        base_url = "http://dominion.diehrstraits.com/"
        data_url = "{}?set=All&f=list".format(base_url)
        html = requests.get(data_url).text
        soup = bs(html)

        for card_set in soup.findAll("table"):
            for row in card_set.findAll("tr"):
                cols = row.findAll("td")
                if cols:
                    card = Card()

                    card.name = strip_tags(cols[1].text)

                    card.card_set, created = CardSet.objects.get_or_create(
                        name=strip_tags(cols[2].text)
                    )
                    if created:
                        card.card_set.save()

                    card.card_type, created = CardType.objects.get_or_create(
                        name=strip_tags(cols[3].text)
                    )
                    if created:
                        card.card_type.save()

                    total_cost = strip_tags(cols[4].text).split(" ")

                    card.cost_gold = total_cost[0].replace("$", "")
                    if len(total_cost) > 1:
                        card.cost_potions = total_cost[1].replace("P", "")
                    else:
                        card.cost_potions = 0

                    card.rules = strip_tags(cols[5].text)

                    card.image_url = "{}scans/{}/{}.jpg".format(
                        base_url,
                        card.card_set.name.replace(" ", "").lower(),
                        card.name.replace(" ", "").replace("'", "").replace("-", "").lower(),
                    )

                    card.save()
                    self.log_message(card)
