import django_filters
from django_filters import DateFilter

from books import forms
from books.models import Book


# lookup_expr -> icontains, startswith, endswith, lte, lt, gte, gt
# gte - greater than or equal to
# gt- greater than

# lte - lower than or equal to
# lt - lower than

class BookFilter(django_filters.FilterSet):
    book_name = django_filters.CharFilter(lookup_expr='icontains', label='Book Name')
    author1 = django_filters.CharFilter(lookup_expr='icontains', label='First Author')
    author2 = django_filters.CharFilter(lookup_expr='icontains', label='Second Author')
    # start_date_gte = DateFilter(field_name='start_date', lookup_expr='gte', label='From start date',
    #                             widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    # start_date_lte = DateFilter(field_name='start_date', lookup_expr='lte', label='To start date',
    #                             widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    #
    # end_date_gte = DateFilter(field_name='end_date', lookup_expr='gte', label='From end date',
    #                           widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    # end_date_lte = DateFilter(field_name='end_date', lookup_expr='lte', label='To end date',
    #                           widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

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
