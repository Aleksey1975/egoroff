from django.http import HttpResponse
from django.shortcuts import render

def day_of_week(request, day):
    if day.lower() not in 'ttt':
        return HttpResponse('Нет такого дня недели!')

    return HttpResponse(day)
