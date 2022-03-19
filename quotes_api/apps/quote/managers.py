from djongo import models
from django.utils import timezone

class QuoteManager(models.DjongoManager):
    def create_quote(self, data):
        quote = self.create(
            content=data['content'],
            author=data['author'],
            enabled=True,
            date=timezone.now(),
        )
        return quote
    
class CommentManager(models.DjongoManager):
    def create_to_quote(self, data):
        comment = self.create(
            content=data['content'],
            date=timezone.now(),
        )
        return comment