from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Olá, {} de {} anos'.format(nome, idade))