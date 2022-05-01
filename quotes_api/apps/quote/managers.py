from djongo.models import Q
from django.utils import timezone
from . import queries

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
                queries.votes_projection(device_id)
            ]
        )
        return quotes
    
    def read(self, _id, device_id):
        quotes = self.mongo_aggregate(
            [
                {'$match': {'_id': _id}},
                queries.votes_projection(device_id)
            ]
        )
        quote = None
        try:
            quote = quotes.next()
        except:
            pass
        
        return quote
    
    def search(self, query, device_id):
        quotes = self.mongo_aggregate(
            [
                queries.searc_match(query),
                queries.votes_projection(device_id)
            ]
        )
        print('search', quotes)
        return quotes
    
   