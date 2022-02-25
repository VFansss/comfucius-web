# pylint: disable=no-member
import random

from django.db import models
from django.urls import reverse

# Create your models here.

class Phrase(models.Model):
    text = models.TextField(blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("phrases:phrase-display", kwargs={"my_id": self.id})

    # define a standard phrase for when I can't retrieve anything from DB
    @staticmethod
    def get_default_value():
        return "..."

    @staticmethod
    def get_random():
        return random.choice(Phrase.objects.all()).text

class Thinker(models.Model):
    name = models.TextField(blank=False, null=False)

    # define a standard value for when I can't retrieve anything from DB
    @staticmethod
    def get_default_value():
        return "Qualcuno"

    @staticmethod
    def get_random():
        return random.choice(Thinker.objects.all()).name
