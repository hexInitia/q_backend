from rest_framework import serializers
from .models import Comment
from quotes_api.apps.generic.serializers import CommentableModelSerializer


class CommentSerializer(CommentableModelSerializer,serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = CommentableModelSerializer.Meta.fields + ['original_quote',
                                                           'original_comment',
                                                           'original_suggestion']
        
class CommentToQuoteSerializer(serializers.Serializer):
    content = serializers.CharField(required=True)
    quote_id = serializers.CharField(required=True)
    
class CommentToCommentSerializer(serializers.Serializer):
    content = serializers.CharField(required=True)
    comment_id = serializers.CharField(required=True)
    
class CommentToSuggestionSerializer(serializers.Serializer):
    content = serializers.CharField(required=True)
    suggestion_id = serializers.CharField(required=True)
    
class CommentsFromQuoteSerializer(serializers.Serializer):
    quote_id = serializers.CharField(required=True)
    device_id = serializers.CharField(required=True)
    page = serializers.IntegerField(required=True)
    
class CommentsFromCommentSerializer(serializers.Serializer):
    comment_id = serializers.CharField(required=True)
    device_id = serializers.CharField(required=True)
    page = serializers.IntegerField(required=True)

class CommentsVotesSerializer(serializers.Serializer):
    comment_id = serializers.CharField(required=True)
    device_id = serializers.CharField(required=True)
    positive = serializers.BooleanField(required=True)