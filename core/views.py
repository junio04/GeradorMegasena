from django.shortcuts import render
import random


def mega(request):
    lista = []

    tamanho_lista = 6

    i = 0

    while i < tamanho_lista:
        lista.append(random.randint(1, 60))
        i = i + 1

    return render(request, 'index.html', {'lista': lista})


def error404(request, exception):
    return render(request, 'error404.html', status=404)