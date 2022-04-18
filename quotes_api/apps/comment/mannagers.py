from djongo import models
from django.utils import timezone

class CommentManager(models.DjongoManager):
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
    
    def comments_from_quote(self, device_id, original_quote):
        comments = self.mongo_aggregate(
                [
                    {
                        '$match': {
                            'original_quote': original_quote
                        }
                    },
                    {
                        '$project': {
                            '_id': '$_id',
                            'content': 'content',
                            'original_quote': '$original_quote',
                            'ups_count': '$ups_count',
                            'downs_count': '$downs_count',
                            'comments': '$comments',
                            'comments_count': '$comments_count',
                            'date': '$date',
                            
                            "ups": {
                                '$in': [device_id, '$ups']
                            },
                            "downs": {
                                '$in': [device_id, '$downs']
                            }
                        }
                    }
                ]
            )
        return comments
    
    def comments_from_comment(self, device_id, original_comment):
        comments = self.mongo_aggregate(
                [
                    {
                        '$match': {
                            'original_comment': original_comment
                        }
                    },
                    {
                        '$project': {
                            '_id': '$_id',
                            'content': 'content',
                            'original_quote': '$original_quote',
                            'original_comment': '$original_comment',
                            'ups_count': '$ups_count',
                            'downs_count': '$downs_count',
                            'comments': '$comments',
                            'comments_count': '$comments_count',
                            'date': '$date',
                            
                            "ups": {
                                '$in': [device_id, '$ups']
                            },
                            "downs": {
                                '$in': [device_id, '$downs']
                            }
                        }
                    }
                ]
            )
        return comments
    
    def update_ups(self, _id, device_id):
        comment = self.filter(_id=_id).first()
        if comment is not None:
            if device_id in comment.downs:
                comment.downs.remove(device_id)
                comment.downs_count -= 1
            if device_id in comment.ups:
                comment.ups.remove(device_id)
                comment.ups_count -= 1
            else:
                comment.ups.append(device_id)
                comment.ups_count += 1
            
            comment.save()
        
        return comment
    
    def update_downs(self, _id, device_id):
        comment = self.filter(_id=_id).first()
        if comment is not None:
            if device_id in comment.ups:
                comment.ups.remove(device_id)
                comment.ups_count -= 1
            if device_id in comment.downs:
                comment.downs.remove(device_id)
                comment.downs_count -= 1
            else:
                comment.downs.append(device_id)
                comment.downs_count += 1
                
            comment.save()
        return comment