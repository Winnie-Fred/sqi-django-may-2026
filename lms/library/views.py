from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Book

# Create your views here.

def home(request):
    return render(request, "library/home.html")

def book_list(request):
    all_books = Book.objects.all()
    return render(request, "library/book_list.html", {"all_books": all_books})


def book_detail(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    return render(request, "library/book_detail.html", {"book": book})
