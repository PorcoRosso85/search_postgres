from django.urls import path

from . import views

urlpatterns = [
        path('', views.QuoteList.as_view(), name='quote'),
        path('searchresults/', views.SearchResultsList.as_view(), name='searchresults')
        ]
