from django.urls import path
from . import views


urlpatterns = [
    path('', views.money_list, name='money_list'),
]
