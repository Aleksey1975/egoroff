from django.shortcuts import render

def index_gor(request):
    return render(request, 'goroscope/index_gor.html')
