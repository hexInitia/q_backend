from django.urls import path
from .views import *

app_name = 'quotes_api.apps.quote'

urlpatterns = [
    path('comment/create', CreateCommentView.as_view()),
    path('api/quotes/create', QuotesCreateView.as_view()),
    path('api/comments/to_quote', CommentToQuoteView.as_view()),
    path('api/comments/to_comment', CommentToCommentView.as_view()),
    path('api/quotes/up/update', QuotesUpUpdateView.as_view()),
    path('api/quotes/down/update', QuotesDownUpdateView.as_view()),
    path('api/comments/up/update', CommentsUpUpdateView.as_view()),
    path('api/comments/down/update', CommentsDownUpdateView.as_view()),
]