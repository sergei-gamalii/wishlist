from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})  # пустой словарь - это контекст