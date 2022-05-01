from rest_framework import serializers
from .models import *
from quotes_api.apps.generic.serializers import CommentableModelSerializer


class QuoteSerializer(CommentableModelSerializer,serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = CommentableModelSerializer.Meta.fields + ['author',
            'enabled', 'days_to_die',  'background_color',
            'font_family']
        
class QuotesCreateSerializer(serializers.Serializer):
    author = serializers.CharField(required=True)
    content = serializers.CharField(required=True)
    font_family = serializers.CharField()
    background_color = serializers.CharField()
    
class QuotesHomeSerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True)
    page = serializers.IntegerField(required=True)
    
class QuoteReadSerializer(serializers.Serializer):
    quote_id = serializers.CharField(required=True)
    device_id = serializers.CharField(required=True)
    
class QuotesSearchSerializer(serializers.Serializer):
    query = serializers.CharField(required=True)
    device_id = serializers.CharField(required=True)
        
class QuotesVotesSerializer(serializers.Serializer):
    quote_id = serializers.CharField(required=True)
    device_id = serializers.CharField(required=True)
    positive = serializers.BooleanField(required=True)