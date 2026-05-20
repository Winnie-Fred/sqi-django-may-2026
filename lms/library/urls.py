from django.urls import path

from . import views

app_name = "library"

urlpatterns = [
    path('', views.home, name='home'),
    path('book-list/', views.book_list, name='book_list'),
    path('books/<int:book_pk>/', views.book_detail, name='book_detail'),
]