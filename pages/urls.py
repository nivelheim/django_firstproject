from django.urls import path
from . import views

app_name='pages'
urlpatterns = [
    path('main/', views.indexView, name='index'),
    path('works/', views.workView, name='works'),
    path('biography/', views.bioView, name='biography'),
    path('contact/', views.contactView, name='contact')
    #path('works/', WorkView.as_view(), name='works'),
    #path('bio/', views.BioView, nama='biography')
]
