from django.urls import path

from . import views

app_name = "library"

urlpatterns = [
    path('', views.home, name='home'),
    path('book-list/', views.book_list, name='book_list'),
    path('books/<int:book_pk>/', views.book_detail, name='book_detail'),
    path('create/book/', views.create_book_model_form, name="create_book_model_form"),
    path('create/book/simple/', views.create_book_simple_form, name="create_book_simple_form"),
    path('update_book_model_form/<int:book_id>/', views.update_book_model_form, name="update_book_model_form"),
]