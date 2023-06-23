from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def get_rectangle_area(request, width, height):
    return HttpResponse(f'Площадь прямоугольника размером {width} X {height} равна {width * height}.')

def get_square_area(request, width):
    return HttpResponse(f'Площадь квадрата размером {width} X {width} равна {width * width}.')


def get_circle_area(request, width):
    return HttpResponse(f'Площадь круга радиуса {width} равна {width**2 * 3.14}.')



def fail(request, m):
    return HttpResponseNotFound('Не могу вычислить площадь фигуры!')