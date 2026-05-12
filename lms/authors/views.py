from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def all_authors(request):
    return render(request, "authors/author_list.html")

def book_signings(request):
    return render(request, "authors/book_signings.html")