from djongo import models

class CommentableManager(models.DjongoManager):
    def update_votes(self, _id, device_id, positive):
        obj = self.filter(_id=_id).first()
        if obj is not None:
            if positive:
                obj = self._up_vote(obj, device_id)
            else:
                obj = self._down_vote(obj, device_id)  
        return obj
    
    def _up_vote(self, obj, device_id):
        if device_id in obj.downs:
            obj.downs.remove(device_id)
            obj.votes += 1
        if device_id in obj.ups:
            obj.ups.remove(device_id)
            obj.votes -= 1
        else:
            obj.ups.append(device_id)
            obj.votes += 1
        obj.save()
        return obj
    
    def _down_vote(self, obj, device_id):
        if device_id in obj.ups:
            obj.ups.remove(device_id)
            obj.votes -= 1
        if device_id in obj.downs:
            obj.downs.remove(device_id)
            obj.votes += 1
        else:
            obj.downs.append(device_id)
            obj.votes -= 1
        obj.save()
        return obj