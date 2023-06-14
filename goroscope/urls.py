from django.urls import path
from .views import *



urlpatterns = [
    path('', index_gor, name='index_gor'),
]
