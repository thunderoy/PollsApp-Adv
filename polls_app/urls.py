from django.urls import path
from . import views

app_name = 'polls_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('<int:pk>/vote/', views.vote, name='vote'),
    path('<int:pk>/result/', views.result, name='result'),
]