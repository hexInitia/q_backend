from djongo import models
from .managers import *
from quotes_api.apps.generic.models import CommentableModel

class Suggestion(CommentableModel):
    objects = SuggestionManager()
    def __str__(self):
        return "{}".format(self._id)
    
