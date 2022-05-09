from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import CreateSuggestionSerializer


class CreateSuggestionView(APIView):
    def post(self, request):
        data = CreateSuggestionSerializer(data=request.data)
        if data.is_valid():
            suggestion = Suggestion.objects.create_suggestion(
                content=data.validated_data['content'])
            if suggestion is not None:
                return Response(data={'ok':True,
                                      'message': 'Suggestion created successfully {}'.format(suggestion._id)})
            else:
                return Response(data={'ok':False, 'message':'error creating suggestion'})
        else:
            return Response(data={'ok':False, 'message':data.errors})