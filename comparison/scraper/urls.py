from django.urls import path, include

from . import views


app_name = 'scraper'

urlpatterns = [
    path('', views.SearchView.as_view(), name='search_view'),
    path('result/', views.ResultView.as_view(), name='result'),
]

#done