from djongo import models
from djongo.models import Q
from django.utils import timezone

class QuoteManager(models.DjongoManager):
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
    
    def update_ups(self, _id, device_id,):
        quote = self.filter(_id=_id).first()
        if quote is not None:
            if device_id in quote.downs:
                    quote.downs.remove(device_id)
                    quote.downs_count -= 1
            if device_id in quote.ups:
                quote.ups.remove(device_id)
                quote.ups_count -= 1
            else:
                quote.ups.append(device_id)
                quote.ups_count += 1
                
            quote.save()
        return quote
    
    def update_downs(self, _id, device_id):
        quote = self.filter(_id=_id).first()
        if quote is not None:
            if device_id in quote.ups:
                    quote.ups.remove(device_id)
                    quote.ups_count -= 1
            if device_id in quote.downs:
                quote.downs.remove(device_id)
                quote.downs_count -= 1
            else:
                quote.downs.append(device_id)
                quote.downs_count += 1
                
            quote.save()
        return quote
    
    def search(self, query):
        quotes = self.filter(
            Q(author__contains=query) |
            Q(content__contains=query) 
        )
        print(quotes)
        return quotes