from django.urls import path
from .views import *

urlpatterns = [
    path('', index_gor, name='index_gor'),
    path('<sing_slug>/', sing_slug, name='sing_slug'),

]
