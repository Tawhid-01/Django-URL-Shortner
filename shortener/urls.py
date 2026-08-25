from django.urls import path
from .views import home_view, redirect_view

urlpatterns = [
    path('', home_view, name='home'),
    path('<str:short_code>/', redirect_view, name='redirect'),
   
]