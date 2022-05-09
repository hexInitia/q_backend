from djongo import models
from quotes_api.apps.generic.models import CommentableModel

class Suggestion(CommentableModel):
    def __str__(self):
        return "{}".format(self._id)