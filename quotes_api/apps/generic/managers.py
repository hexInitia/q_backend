from djongo import models

class CommentableManager(models.DjongoManager):
    def update_votes(self, _id, device_id, positive):
        quote = self.filter(_id=_id).first()
        if quote is not None:
            if positive:
                quote = self._up_vote(quote, device_id)
            else:
                quote = self._down_vote(quote, device_id)  
        return quote
    
    def _up_vote(self, quote, device_id):
        if device_id in quote.ups:
            quote.ups.remove(device_id)
            quote.votes -= 1
        else:
            print("up vote")
            quote.ups.append(device_id)
            quote.votes += 1
        quote.save()
        return quote
    
    def _down_vote(self, quote, device_id):
        if device_id in quote.downs:
            quote.downs.remove(device_id)
            quote.votes += 1
        else:
            quote.downs.append(device_id)
            quote.votes -= 1
        quote.save()
        return quote