from djongo import models
from django.utils import timezone

from quotes_api.apps.generic import constants
from . import queries
from quotes_api.apps.generic.managers import CommentableManager

class CommentManager(CommentableManager):
    def create_to_quote(self, data, quote):
        comment = self.create(
            content=data['content'],
            original_quote=data['quote_id'],
            date=timezone.now(),
        )
        quote.comments.append(str(comment._id))
        quote.comments_count += 1
        quote.save()
        return comment
    
    def create_to_comment(self, data, to_comment):
        print(data)
        comment = self.create(
            content=data['content'],
            original_comment=to_comment._id,
            date=timezone.now(),
        )
        to_comment.comments.append(str(comment._id))
        to_comment.comments_count += 1
        to_comment.save()
        return comment
    
    def comments_from_quote(self, device_id, original_quote, page):
        comments = self.mongo_aggregate(
                [
                    {
                        '$match': {
                            'original_quote': original_quote
                        }
                    },
                    {'$skip': page * constants.PAGE_SIZE},
                    {'$limit': constants.PAGE_SIZE},
                    {'$sort': {'votes': -1}},
                    queries.votes_projection(device_id)
                ]
            )
        return comments
    
    def comments_from_comment(self, device_id, original_comment, page):
        comments = self.mongo_aggregate(
                [
                    {
                        '$match': {
                            'original_comment': original_comment
                        }
                    },
                    {'$skip': page * constants.PAGE_SIZE},
                    {'$limit': constants.PAGE_SIZE},
                    queries.votes_projection(device_id)
                ]
            )
        return comments