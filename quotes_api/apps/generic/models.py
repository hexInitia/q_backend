from djongo import models

# Create your models here.

class CommentableModel(models.Model):
    _id = models.ObjectIdField(primary_key=True, db_column='_id')
    content = models.TextField()
    ups = models.JSONField(blank=True, null=True, default=list)
    downs = models.JSONField(blank=True, null=True, default=list)
    comments = models.JSONField(blank=True, null=True, default=list)
    comments_count = models.PositiveIntegerField(default=0)
    date = models.DateTimeField()
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return "{}".format(self._id)