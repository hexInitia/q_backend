from django.urls import path
from .views import *

app_name = 'quotes_api.apps.suggestion'

urlpatterns = [
    path('api/suggestion/create', CreateSuggestionView.as_view(), name='create'),
    path('api/suggestion/read', ReadSuggestionView.as_view(), name='create'),
]