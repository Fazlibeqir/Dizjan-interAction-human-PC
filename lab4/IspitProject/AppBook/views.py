from django.shortcuts import render, redirect

from AppBook.forms import BookForm
from AppBook.models import Book


# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})


def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'booksDetail.html', {'book': book})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})
