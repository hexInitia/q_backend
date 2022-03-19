from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
# Create your views here.


class CreateCommentView(APIView):
    def post(self, request):
        comment = CommentSerializer(data=request.data)
        print(request.data)
        if comment.is_valid():
            print(comment.validated_data)
            comment.save()
            return Response(data={'success': True})
        else:
            print(comment.errors)
            return Response(data={'success': False, 'errors': comment.errors})
        
class QuotesCreateView(APIView):
    def post(self, request):
        data=QuotesCreateSerializer(data=request.data)
        if data.is_valid():
            print(data.validated_data)
            quote = Quote.objects.create_quote(data.validated_data)
            print(quote)
            js = QuoteSerializer(quote)
            return Response(data={'ok': True,
                                  'message': 'quote created successfully',
                                  'quotes': [js.data]
                                  })
        else:
            return Response(data={'ok': False, 'message': data.errors})
