from django.urls import path

from .views import *

urlpatterns = [
    path('<int:number>/', number_of_week),
    path('<da>/', day_of_week, name='day_of_week'),


]