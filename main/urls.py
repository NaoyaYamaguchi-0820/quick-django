from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('temp', views.temp, name='temp'),
    path('list', views.list, name='list'),
    path('iftag', views.iftag, name='iftag'),
    path('yesno', views.yesno, name='yesno'),
    path('firstof', views.firstof, name='firstof'),
    path('master', views.master, name='master'),
    path('static', views.static, name='static'),
    path('filter', views.filter, name='filter'),
    path('rel', views.rel, name='rel'),
    path('rel2', views.rel2, name='rel2'),
    path('route_param', views.route_param, name='route_param'),
    path('route_param/<int:id>', views.route_param, name='route_param'),
    path('displayHttpRequest', views.displayHttpRequest, name='displayHttpRequest'),
    path('req_redirect', views.req_redirect, name='req_redirect'),
    path('req_redirect2', views.req_redirect2, name='req_redirect2'),
    path('res_notfound', views.res_notfound, name='res_notfound'),
    path('res_notfound2', views.res_notfound2, name='res_notfound2'),
    path('res_header', views.res_header, name='res_header'),
    path('res_csv', views.res_csv, name='res_csv'),

]