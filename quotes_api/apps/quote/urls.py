from django.urls import path
from .views import *

app_name = 'quotes_api.apps.quote'

urlpatterns = [
    path('comment/create', CreateCommentView.as_view(), name="create")
]