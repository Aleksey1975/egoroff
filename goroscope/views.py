from django.shortcuts import render

def index_gor(request):
    return render(request, 'goroscope/index_gor.html', {'title':'Гороскоп'})


def lion(request):
    return render(request, 'goroscope/lion.html', {'title':'Лев'})


def rak(request):
    return render(request, 'goroscope/rak.html', {'title':'Рак'})



def vesi(request):
    return render(request, 'goroscope/vesi.html', {'title':'Весы'})



def deva(request):
    return render(request, 'goroscope/deva.html', {'title':'Дева'})