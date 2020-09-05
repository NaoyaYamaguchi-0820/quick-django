from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
import random

# Create your views here.

def index(request):
    return HttpResponse('indexメソッド')

def temp(request):

    context = {
        'msg': 'こんにちは、世界'
    }

    return render(request, 'main/temp.html', context)

def list(request):
    books = Book.objects.all()

    return render(request, 'main/list.html', {
        'books': books,
    })

def iftag(request):
    return render(request, 'main/iftag.html',{
        'random': random.randint(0, 100),
    })

def yesno(request):
    return render(request, 'main/yesno.html', {
        'flag': None
    })

def firstof(request):
    return render(request, 'main/firstof.html', {
        'a': 'hello.',
        'b': 'good evening.',
        'c': 'good night.',
    })