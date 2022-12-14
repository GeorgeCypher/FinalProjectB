from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from books.filters import BookFilter
from books.forms import BookUpdateForm, BookForm
from books.models import Book
from django.http import FileResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
# from .forms import UploadFileForm


class BookCreateView(CreateView):
    template_name = 'books/add_book.html'
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('homepage')

class BookListView(ListView):
    template_name = 'books\list_of_books.html'
    model = Book
    context_object_name = 'all_books'

    def get_queryset(self):
        return Book.objects.all().order_by('book_name')

    def get_context_data(self, **kwargs):
        data = super(BookListView, self).get_context_data(**kwargs)
        # data['trainers'] = Trainer.objects.all()

        books = Book.objects.all()
        myFilter = BookFilter(self.request.GET, queryset=books)
        books = myFilter.qs

        data['all_books'] = books
        data['my_filter'] = myFilter

        return data


class BookUpdateView(UpdateView):
    template_name = 'books/update_book.html'
    model = Book
    form_class = BookUpdateForm
    success_url = reverse_lazy('list_of_books')


class BookDeleteView(DeleteView):
    template_name = 'books/delete_book.html'
    model = Book
    success_url = reverse_lazy('list_of_books')
    permission_required = 'book.delete_book'


# @permission_required('model.codename'), ex: @permission_required('books.delete_book')
# @permission_required('books.delete_book')
def delete_book_by_modal(request, pk):
    Book.objects.filter(id=pk).delete()
    return redirect('list_of_books')


class BookDetailView(DetailView):
    template_name = 'books/details_book.html'
    model = Book
    permission_required = 'book.view_book'
