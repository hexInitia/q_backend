from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from quotes_api.apps.quote.models import Quote
from .serializers import *
from .models import *
from bson import ObjectId
from quotes_api.apps.utils import check_request_param as rp

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
        
class CommentToQuoteView(APIView):
    def post(self, request):
        print(request.query_params)
        
        data=CommentToQuoteSerializer(data={
            'content': request.data['content'],
            'quote_id': rp(request, 'quote_id'),
            })
        if data.is_valid():
            print(data.validated_data)
            quote = Quote.objects.filter(_id = ObjectId(data.validated_data['quote_id'])).first()
            if quote is not None:
                comment = Comment.objects.create_to_quote(data.validated_data, quote)
                
                js = CommentSerializer(comment)
                return Response(data={'ok':True,
                                      'message': 'comment created successfully',
                                      'comments': [js.data]})
            else:
                return Response(data={'ok':False, 'message':'invalid quote id'})
                
        else:
            return Response(data={'ok':False, 'message': data.errors})

    
class CommentToCommentView(APIView):
    def post(self, request):
        print(request.query_params)
        
        data=CommentToCommentSerializer(data={
            'content': request.data['content'],
            'comment_id': rp(request, 'comment_id'),
            })
        if data.is_valid():
            print(data.validated_data)
            to_comment = Comment.objects.filter(_id = ObjectId(data.validated_data['comment_id'])).first()
            if to_comment is not None:
                comment = Comment.objects.create_to_comment({
                    'content': data.validated_data['content']
                }, to_comment)
                
                js = CommentSerializer(comment)
                return Response(data={'ok':True,
                                      'message': 'comment created successfully',
                                      'comments': [js.data]})
            else:
                return Response(data={'ok':False, 'message':'invalid comment id'})
                
        else:
            return Response(data={'ok':False, 'message': data.errors})
    
    
    
class CommentsFromQuoteView(APIView):
    def get(self, request):
        data=CommentsFromQuoteSerializer(data={
            'quote_id': rp(request,'quote_id'),
            'device_id': rp(request,'device_id'),
            'page': rp(request,'page'),
        })
        if data.is_valid():
            print(data.validated_data)
            device_id = data.validated_data['device_id']
            quote_id = data.validated_data['quote_id']
            page = data.validated_data['page']
            comments = Comment.objects.comments_from_quote(device_id, quote_id, page)
            
            js = CommentSerializer(comments, many=True).data
                            
            return Response(data={'ok': True, 'message': 'list of comments',
                                  'comments':js})
        else:
            return Response(data={'ok':False, 'message': data.errors})
        
class CommentsFromCommentView(APIView):
    def get(self, request):
        data=CommentsFromCommentSerializer(data={
            'comment_id': rp(request,'comment_id'),
            'device_id': rp(request,'device_id'),
            'page': rp(request,'page'),
        })
        if data.is_valid():
            print(data.validated_data)
            device_id = data.validated_data['device_id']
            comment_id = data.validated_data['comment_id']
            page = data.validated_data['page']
            
            comments = Comment.objects.comments_from_comment(device_id, comment_id, page)
            
            js = CommentSerializer(comments, many=True).data
                            
            return Response(data={'ok': True, 'message': 'list of comments',
                                  'comments':js})
        else:
            return Response(data={'ok':False, 'message': data.errors})
        
      
class CommentsVotesUpdateView(APIView):
    def put(self, request):
        data=CommentsVotesSerializer(data={
            'comment_id': rp(request,'comment_id'),
            'device_id': rp(request,'device_id'),
            'positive': rp(request,'positive'),
        })
        if data.is_valid():
            print(data.validated_data)
            comment = Comment.objects.update_votes(
                device_id = data.validated_data['device_id'],
                _id=ObjectId(data.validated_data['comment_id']),
                positive=data.validated_data['positive'])
            if comment is not None:
                return Response(data={'ok': True, 'message': 'comment ups updated successfully'})
            else:
                return Response(data={'ok':False, 'message': 'invalid comment id'})
        else:
            return Response(data={'ok':False, 'message': data.errors})