from django.shortcuts import render
from django.http import HttpResponse

from .models import Author


# Create your views here.

def all_authors(request):
    return render(request, "authors/author_list.html")

def book_signings(request):
    return render(request, "authors/book_signings.html")

def model_in_view(request):
    all_authors = Author.objects.all()
    # authors_born_before_1950 = all_authors.filter(birth_date__lte="1950-01-01")
    authors_born_before_1950 = all_authors.filter(birth_date__year__lt=1950)

    all_authors_desc = all_authors.order_by("-first_name")

    author_pk_7 = Author.objects.get(pk=7)

    try:
        nonexistent_author = Author.objects.get(pk=1000)
    except Author.DoesNotExist:
        nonexistent_author = None

    context = {
        "all_the_authors": all_authors,
        "authors_born_before_1950": authors_born_before_1950,
        "all_authors_desc": all_authors_desc,
        "author_pk_7": author_pk_7,
        "nonexistent_author": nonexistent_author,
    }
    return render(request, "authors/model-in-view.html", context)