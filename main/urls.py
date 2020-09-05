from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('temp', views.temp, name='temp'),
    path('list', views.list, name='list'),
    path('iftag', views.iftag, name='iftag'),
    path('yesno', views.yesno, name='yesno'),
    path('firstof', views.firstof, name='firstof'),

]