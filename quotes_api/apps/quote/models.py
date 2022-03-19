from djongo import models

# Create your models here.

class CommentableModel(models.Model):
    _id = models.ObjectIdField(primary_key=True, db_column='_id')
    content = models.TextField()
    ups = models.JSONField(blank=True, null=True, default=list)
    ups_count = models.PositiveIntegerField()
    downs = models.JSONField(blank=True, null=True, default=list)
    downs_count = models.PositiveIntegerField()
    comments = models.JSONField(blank=True, null=True, default=list)
    comments_count = models.PositiveIntegerField()
    date = models.DateField()
    class Meta:
        abstract = True

class Quote(CommentableModel):
    author = models.TextField()
    enabled = models.BooleanField()
    days_to_die = models.PositiveIntegerField(default=7)

    class Meta:
        db_table = 'Quote'
    def __str__(self):
        return "{} {}".format(self._id, self.author)


class Comment(CommentableModel):
    class Meta:
        db_table = 'Comment'
    
    def __str__(self):
        return "{}".format(self._id)