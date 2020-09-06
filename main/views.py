from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
import random
from datetime import date
from django.db.models import Q
from django.db.models.functions import Substr
from django.shortcuts import redirect
from django.http import Http404
from django.shortcuts import get_object_or_404
import csv

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

def master(request):
    return render(request, 'main/master.html', {
        'msg': 'masterです',
    })

def static(request):
    return render(request, 'main/static.html',)

def filter(request):
    books = Book.objects.values('title', 'price')

    return render(request, 'main/list.html',{
        'books': books
    })

def rel(request):
    return render(request, 'main/rel.html', {
        'book': Book.objects.get(pk=1),
    })

def rel2(request):
    return render(request, 'main/rel2.html', {
        'books': Book.objects.all(),
    })

def route_param(request, id=-1):
    return HttpResponse(f'id値:{id}')

def displayHttpRequest(request):
    return HttpResponse(f'リクエストヘッダー：{request.headers["User-Agent"]}')

def req_redirect(request):
    return redirect('list')

def req_redirect2(request):
    return redirect('route_param', id=10)

def res_notfound(request):
    try:
        book = Book.objects.get(pk=108)
    except Book.DoesNotExist:
        raise Http404('指定の書籍情報が存在しません。')

    return render(request, 'main/book_detail.html', {
        'book': book
    })

def res_notfound2(request):
    book = get_object_or_404(Book, pk=108)
    return render(request, 'main/book_detail.html', {
        'book': book
    })

def res_header(request):
    response = HttpResponse('<message>Hello,World!!</message>', content_type='text/xml')
    response['Content-Disposition'] = 'attachment;filename="hoge.xml"'
    return response

def res_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="data.csv"'
    
    writer = csv.writer(response)
    writer.writerows([
        ['tyamada', '山田太郎', '30'],
        ['ksuzuki', '鈴木健司', '26'],
        ['itanaka', '田中一郎', '34'],
    ])

    return response