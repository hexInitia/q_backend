from rest_framework import serializers
from .models import *
from quotes_api.apps.generic.serializers import CommentableModelSerializer


class CreateSuggestionSerializer(serializers.Serializer):
    content = serializers.CharField(required=True)
    
class SuggestionReadSerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True)
    page = serializers.IntegerField(required=True)
    
class SuggestionSerializer(CommentableModelSerializer):
    class Meta:
        model = Suggestion