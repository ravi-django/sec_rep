from django.urls import path

from testApp import views

urlpatterns = [
    path('index/', views.index_view, name='index_view'),
    path('addmovie/', views.add_movie_view, name='add_movie_view'),
    path('listmovie/', views.list_movie_view, name='list_movie_view')
]
