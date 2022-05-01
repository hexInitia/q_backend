from rest_framework import serializers

class CommentableModelSerializer(serializers.Serializer):
    _id = serializers.CharField(required=False)
    content = serializers.CharField(default="")
    ups = serializers.JSONField(required=False)
    downs = serializers.JSONField(required=False)
    comments = serializers.JSONField(required=False)
    comments_count = serializers.IntegerField(default=0)
    date = serializers.DateTimeField(required=False)
    votes = serializers.IntegerField(default=0)
    
    class Meta:
        fields = ['_id', 'content', 'ups', 'downs','votes',
            'comments', 'comments_count', 'date',]
        
