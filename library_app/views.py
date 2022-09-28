from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Book

# Create your views here.

class BooksList(ListView):
    model = Book
    template_name = 'library_app/books.html'

    def get_context_data(self, **kwargs):
        context = super(BooksList, self).get_context_data(**kwargs)
        available_books = Book.objects.filter(status__startswith='a')
        context['available_books'] = available_books
        available_books_count = available_books.count()
        context['available_books_count'] = available_books_count
        issued_books = Book.objects.filter(status__startswith='i')
        context['issued_books'] = issued_books
        return context


class IssueBook(UpdateView):
    model = Book
    fields = []
    template_name = 'library_app/issue_return.html'

    def post(self, request, pk):
        book = Book.objects.get(id=pk)
        if request.method == "POST":
            book.status = "Issued by someone"
            book.save()
            return redirect('Home')

    def get_context_data(self, **kwargs):
        context = super(IssueBook, self).get_context_data(**kwargs)
        context['type'] = 'issue'
        return context


class ReturnBook(UpdateView):
    model = Book
    fields = []
    template_name = 'library_app/issue_return.html'

    def post(self, request, pk):
        book = Book.objects.get(id=pk)
        if request.method == "POST":
            book.status = "Available for issuing"
            book.save()
            return redirect('Home')