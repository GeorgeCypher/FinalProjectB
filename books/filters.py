import django_filters
from django_filters import DateFilter

from books import forms
from books.models import Book


class BookFilter(django_filters.FilterSet):
    book_name = django_filters.CharFilter(lookup_expr='icontains', label='Book Name')
    author1 = django_filters.CharFilter(lookup_expr='icontains', label='First Author')
    author2 = django_filters.CharFilter(lookup_expr='icontains', label='Second Author')

    class Meta:
        model = Book
        fields = ['book_name', 'author1', 'author2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['book_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter book name'})
        self.filters['author1'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter first author name'})
        self.filters['author2'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter second author name'})
