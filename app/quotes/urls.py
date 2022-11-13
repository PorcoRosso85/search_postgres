from django.urls import path

from . import views

urlpatterns = [
        path('', views.QuoteList.as_view(), name='quote')
        ]
