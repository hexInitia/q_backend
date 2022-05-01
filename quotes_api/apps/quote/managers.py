from djongo import models
from djongo.models import Q
from django.utils import timezone

from quotes_api.apps.generic.managers import CommentableManager

class QuoteManager(CommentableManager):
    def create_quote(self, data):
        quote = self.create(
            content=data['content'],
            author=data['author'],
            background_color=data['background_color'],
            font_family=data['font_family'],
            enabled=True,
            date=timezone.now(),
        )
        return quote
    
    def find_random_home(self, device_id):
        quotes = self.mongo_aggregate(
            [
                {'$sample': {'size': 5}},
                {
                    '$project': {
                        '_id': '$_id',
                        'content': '$content',
                        'ups_count': '$ups_count',
                        'downs_count': '$downs_count',
                        'comments_count': '$comments_count',
                        'date': '$date',
                        'author': '$author',
                        'enabled': '$enabled',
                        'days_to_die': '$days_to_die',
                        'background_color': '$background_color',
                        'font_family': '$font_family',
                        'ups': {
                            '$in': [device_id, '$ups']
                        },
                        'downs': {
                            '$in': [device_id, '$downs']
                        }
                    }
                }
            ]
        )
        return quotes
    
    def search(self, query):
        quotes = self.filter(
            Q(author__contains=query) |
            Q(content__contains=query) 
        )
        return quotes
    
   