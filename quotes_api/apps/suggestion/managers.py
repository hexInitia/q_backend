from datetime import date
from djongo import models
from django.utils import timezone

from quotes_api.apps.generic import constants
from quotes_api.apps.suggestion import queries

class SuggestionManager(models.DjongoManager):
    def create_suggestion(self, content):
        suggestion = self.create(
            content=content,
            date=timezone.now()
        )
        return suggestion
    
    def read(self, device_id, page):
        suggestions = self.mongo_aggregate(
            [
                {'$skip': page * constants.PAGE_SIZE},
                {'$limit': constants.PAGE_SIZE},
                {'$sort': {'votes': -1}},
                queries.votes_projection(device_id)
            ]
        )
       
        return suggestions