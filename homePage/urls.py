from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homePage-home'),
    path('about/', views.about, name='homePage-about'),
]