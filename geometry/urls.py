from django.urls import path
from .views import *

urlpatterns = [
    path('rectangle/<int:width>/<int:height>/',get_rectangle_area),
    path('square/<int:width>/', get_square_area),
    path('circle/<int:width>/', get_circle_area),

    path('rectangle/<m>', fail),


]