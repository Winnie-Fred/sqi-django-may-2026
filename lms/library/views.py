from django.shortcuts import render, get_object_or_404, redirect

from .models import Book
from .forms import BookForm

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
