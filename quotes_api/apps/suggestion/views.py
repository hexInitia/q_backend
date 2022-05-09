from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from quotes_api.apps.utils import check_request_param as rp
from bson import ObjectId

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
        
class ReadSuggestionView(APIView):
    def get(self, request):
        data=SuggestionReadSerializer(data={
            'device_id': rp(request,'device_id'),
            'page': rp(request,'page'),
        })
        if data.is_valid():
            suggestions = Suggestion.objects.read(
                device_id = data.validated_data['device_id'],
                page = data.validated_data['page'],
            )
            if suggestions is not None:
                js = SuggestionSerializer(suggestions, many=True).data
                return Response(data={'ok': True,
                                      'message': 'suggestions from the server',
                                      'suggestions': js})
            else:
                return Response(data={'ok': False, 'message': 'invalid suggestion id'})
        else:
            return Response(data={'ok':False, 'message': data.errors}) 