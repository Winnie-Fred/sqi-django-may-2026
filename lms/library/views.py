from django.shortcuts import render, get_object_or_404, redirect

from .models import Book
from .forms import BookForm, BookSimpleForm

# Create your views here.

def home(request):
    return render(request, "library/home.html")

def book_list(request):
    all_books = Book.objects.all()
    return render(request, "library/book_list.html", {"all_books": all_books})


def book_detail(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    return render(request, "library/book_detail.html", {"book": book})


def create_book_model_form(request):
    form = BookForm()

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("library:book_list")
        
    context = {
        "form": form
    }
    return render(request, "library/create-book-model-form.html", context)


def create_book_simple_form(request):
    form = BookSimpleForm()

    if request.method == "POST":
        form = BookSimpleForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            Book.objects.create(
                title=cleaned_data["title"],
                author=cleaned_data["author"],
                number_of_pages=cleaned_data["number_of_pages"],
                published_on=cleaned_data["published_on"],
                cover_image=cleaned_data["cover_image"]
            )
            return redirect("library:book_list")
        
    context = {
        "form": form
    }
    return render(request, "library/create-book-simple-form.html", context)


def update_book_model_form(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    form = BookForm(instance=book)

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("library:book_detail", book_pk=book_id)

    context = {
        "book": book,
        "form": form
    }

    return render(request, "library/update-book-model-form.html", context)


def update_book_simple_form(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    form = BookSimpleForm(initial={
        "title": book.title,
        "author": book.author,
        "number_of_pages": book.number_of_pages,
        "published_on": book.published_on,
        "cover_image": book.cover_image
    })

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            book.title = cleaned_data["title"]
            book.author = cleaned_data["author"]
            book.number_of_pages = cleaned_data["number_of_pages"]
            book.published_on = cleaned_data["published_on"]
            book.cover_image = cleaned_data["cover_image"]
            book.save()
            return redirect("library:book_detail", book_pk=book_id)

    context = {
        "book": book,
        "form": form
    }

    return render(request, "library/update-book-simple-form.html", context)