from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # مسیر اصلی به view home
]
