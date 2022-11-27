from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from books.filters import BookFilter
from books.forms import BookUpdateForm, BookForm
from books.models import Book

from django.http import HttpResponseRedirect
from django.shortcuts import render
# from .forms import UploadFileForm

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# Imaginary function to handle an uploaded file.
# from books import handle_uploaded_file

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'uploads/upload.html', context)

def model_form_upload(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        file = request.FILES['file']
        book_view = Book.objects.create(upload_file=file)
        return render("The document is " + str(file))
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})

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
    success_url = reverse_lazy('list_of_Books')


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
