from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book-list/', views.book_list, name='book_list'),
]