from rest_framework import serializers

class CreateSuggestionSerializer(serializers.Serializer):
    content = serializers.CharField(required=True)