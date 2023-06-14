from django.urls import path
from .views import *

urlpatterns = [
    path('', index_gor, name='index_gor'),
    path('lion/', lion, name='lion'),
    path('deva/', deva, name='deva'),
    path('vesi/', vesi, name='vesi'),
    path('rak/', rak, name='rak'),
]
