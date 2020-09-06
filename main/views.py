from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .forms import BookForm
import random
from datetime import date
from django.db.models import Q
from django.db.models.functions import Substr
from django.shortcuts import redirect
from django.http import Http404
from django.shortcuts import get_object_or_404
import csv
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import BookModelForm
from django.urls import reverse

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

def form_input(request):
    form = BookForm()

    return render(request, 'main/form_input.html',{
        'form': form
    }
    ) 

@require_POST
def form_process(request):
    form = BookForm(request.POST)
    if form.is_valid():
        return render(
            request,
            'main/form_process.html',
            {
                'form': form
            }
        )
    else:
        return render(
            request,
            'main/form_input.html',
            {
                'form': form
            }
        )

def crud_new(request):
    form = BookModelForm()
    return render(
        request,
        'main/crud_new.html',
        {
            'form': form,
        },
    )

@require_POST
def crud_create(request):
    obj = Book()
    form = BookModelForm(request.POST, instance=obj)

    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'データの保存に成功しました')
        return redirect('crud_new')
    else:
        return render(
            request,
            'main/crud_new.html',
            {
                'form': form,
            }
        )

def crud_edit(request, id):
    obj = Book.objects.get(pk=id)
    form = BookModelForm(instance=obj)
    return render(
        request,
        'main/crud_edit.html',
        {
            'id': id,
            'form': form,
        }
    )

@require_POST
def crud_update(request, id):
    obj = Book.objects.get(pk=id)
    form = BookModelForm(request.POST, instance=obj)

    if form.is_valid():
        form.save()
        messages.success(request, 'データの更新に成功しました。')
        return redirect(reverse('crud_edit', kwargs={'id': id}))
    else:
        return render(request, 'main/crud_edit.html', {
            'id': id,
            'form': form,
        })

def crud_show(request, id):
    obj = Book.objects.get(pk=id)
    form = BookModelForm(instance=obj)
    return render(
        request,
        'main/crud_show.html',
        {
            'id': id,
            'form': form,
        }
    )

def crud_delete(request, id):
    obj = Book.objects.get(pk=id)
    obj.delete()
    messages.success(request, 'データの削除に成功しました。')
    return redirect(reverse('list'))