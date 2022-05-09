from django.urls import path
from .views import *

app_name = 'quotes_api.apps.suggestion'

urlpatterns = [
    path('api/suggestions/create', CreateSuggestionView.as_view(), name='create'),
    path('api/suggestions/read', ReadSuggestionView.as_view(), name='create'),
    path('api/suggestions/votes/update', SuggestionVotesUpdateView.as_view(), name='votes_update'),
]