from django.urls import path
from .views import *

urlpatterns = [
    path('', Photo),
    path('sendmsg/', Sendmsg),
    path('create-post/', CreatePost)
]