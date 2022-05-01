from django.urls import path
from .views import *

app_name = 'quotes_api.apps.comment'

urlpatterns = [
    path('comment/create', CreateCommentView.as_view()),
    path('api/comments/to_quote', CommentToQuoteView.as_view()),
    path('api/comments/to_comment', CommentToCommentView.as_view()),
    path('api/comments/from_quote', CommentsFromQuoteView.as_view()),
    path('api/comments/from_comment', CommentsFromCommentView.as_view()),
    path('api/comments/votes/update', CommentsVotesUpdateView.as_view()),
    
]