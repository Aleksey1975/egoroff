from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect

days_of_week = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
def day_of_week(request, da):
    if da not in days_of_week:
        return HttpResponseNotFound('Нет такого дня недели!')

    return HttpResponse(da)

def number_of_week(request, number):
    if number not in (1,2,3,4,5,6,7,8,9):
        return HttpResponseNotFound(f'Нет такого номера дня недели - {number}!')
    d = days_of_week[number - 1]
    return redirect(f'day_of_week', d)
