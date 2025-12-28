from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('assessment/', views.skin_assessment, name='skin_assessment'),
    path('skin_type/', views.skin_type, name='skin_type'),
]