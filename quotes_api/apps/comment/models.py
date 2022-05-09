from djongo import models
from .mannagers import CommentManager
from quotes_api.apps.generic.models import CommentableModel

class Comment(CommentableModel): 
    original_quote = models.TextField(default="")
    original_comment = models.TextField(default="")
    original_suggestion = models.TextField(default="")
    objects = CommentManager()

    def __str__(self):
        return "{}".format(self._id)