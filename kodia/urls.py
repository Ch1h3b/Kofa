
from django.urls import path
from .views import Home, Plus, Delete, getLang

urlpatterns = [
    path('', Home.as_view()),
    path('plus', Plus.as_view()),
    path('delete', Delete.as_view()),
    path('lang', getLang)
]
