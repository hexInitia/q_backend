from django.urls import path
from .views import *

app_name = 'quotes_api.apps.quote'

urlpatterns = [
    path('comment/create', CreateCommentView.as_view()),
    path('api/quotes/create', QuotesCreateView.as_view()),
    path('api/comments/to_quote', CommentToQuoteView.as_view()),
]