from django.urls import path
from . import views

app_name = 'gallery'
urlpatterns = [
    #path('', views.EntityCreateView.as_view(), name='index'),
    #path('', views.upload, name='upload'),
    path('<int:page_id>/', views.page, name='page'),
]
