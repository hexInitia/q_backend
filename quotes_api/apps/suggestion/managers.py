from datetime import date
from djongo import models
from django.utils import timezone

class SuggestionManager(models.DjongoManager):
    def create_suggestion(self, content):
        suggestion = self.create(
            content=content,
            date=timezone.now()
        )
        return suggestion