from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('detailed/', views.detailed_product, name='detailed_product'),
]
