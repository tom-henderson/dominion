import urllib2

from django.db import models
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile


class CardSet(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class CardType(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Card(models.Model):
    name = models.CharField(max_length=30)
    card_set = models.ForeignKey(CardSet)
    card_type = models.ForeignKey(CardType)
    cost_gold = models.IntegerField()
    cost_potions = models.IntegerField()
    rules = models.TextField(max_length=350)
    image_url = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='cards/',
        height_field='image_height',
        width_field='image_width',
        blank=True,
        null=True
    )
    image_height = models.IntegerField(blank=True, null=True)
    image_width = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['card_set', 'name']

    @property
    def cost(self):
        if self.cost_potions > 0:
            return "${} {}P".format(self.cost_gold, self.cost_potions)

        return "${}".format(self.cost_gold)

    def __unicode__(self):
        return "{} ({}) [{}]".format(
            self.name,
            self.card_type,
            self.cost
        )

    def fetch_image(self):
        """
        https://djangosnippets.org/snippets/1890/

        The file reference must be populated with a django.core.files.File
        instance but File cannot handle file-like objects such as those
        returned by urlopen - see http://code.djangoproject.com/ticket/8501

        Since we'd like to get the normal file name collision avoidance,
        automatic location handling, etc. we'll create a django
        NamedTemporaryFile because the default file storage save logic is
        smart enough to simply move the temporary file to the correct location.
        """
        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(urllib2.urlopen(self.image_url).read())
        img_temp.flush()
        self.image.save("{}.jpg".format(
            self.name.lower().replace(" ", "").replace("'", "")
        ), File(img_temp))
