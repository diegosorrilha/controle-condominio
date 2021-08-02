from django.shortcuts import render


def index(request):
    context = {'nome_pagina': 'Início da Dashboard'}

    return render(request, 'index.html', context=context)
