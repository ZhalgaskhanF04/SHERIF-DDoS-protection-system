from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:attack_id>/', views.detail, name = 'detail'),
    path('<int:attack_id>/results', views.results, name = 'results'),
    path('resources',views.resources, name = 'resources'),
]