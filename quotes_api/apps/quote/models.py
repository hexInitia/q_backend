from djongo import models
from .managers import *
from quotes_api.apps.generic.models import CommentableModel

class Quote(CommentableModel):
    author = models.TextField()
    enabled = models.BooleanField()
    days_to_die = models.PositiveIntegerField(default=7)
    objects = QuoteManager()
    background_color = models.TextField()
    font_family = models.TextField()
    
    def __str__(self):
        return "{} {}".format(self._id, self.author)


