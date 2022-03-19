from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from bson import ObjectId
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

class CommentToQuoteView(APIView):
    def post(self, request):
        print(request.query_params)
        
        data=CommentToQuoteSerializer(data={
            'content': request.data['content'],
            'quote_id': self.check_quote_id(request),
            })
        if data.is_valid():
            print(data.validated_data)
            quote = Quote.objects.filter(_id = ObjectId(data.validated_data['quote_id'])).first()
            if quote is not None:
                comment = Comment.objects.create_to_quote(data.validated_data)
                quote.comments.append(str(comment._id))
                quote.comments_count += 1
                quote.save()
                js = CommentSerializer(comment)
                return Response(data={'ok':True,
                                      'message': 'comment created successfully',
                                      'comments': [js.data]})
            else:
                return Response(data={'ok':False, 'message':'invalid quote id'})
                
        else:
            return Response(data={'ok':False, 'message': data.errors})
        return Response(data={'ok':True})
    
    def check_quote_id(self, request):
        if 'quote_id' in request.query_params.keys():
            return request.query_params['quote_id']
        return None