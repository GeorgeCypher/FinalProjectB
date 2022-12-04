import django_filters
from django_filters import DateFilter

from books import forms
from books.models import Book


class BookFilter(django_filters.FilterSet):
    book_name = django_filters.CharFilter(lookup_expr='icontains', label='Book Name')
    author1 = django_filters.CharFilter(lookup_expr='icontains', label='First Author')
    author2 = django_filters.CharFilter(lookup_expr='icontains', label='Second Author')
    editorial = django_filters.CharFilter(lookup_expr='icontains', label='Editorial')
    editorial_city = django_filters.CharFilter(lookup_expr='icontains', label='Editorial City')
    publish_date = django_filters.CharFilter(lookup_expr='icontains', label='Publish Year')
    collection = django_filters.CharFilter(lookup_expr='icontains', label='Collection Name')

    # book_name = models.CharField(max_length=100, null=True, blank=True)
    # author1 = models.CharField(max_length=100, null=True, blank=True)
    # author2 = models.CharField(max_length=100, null=True, blank=True)
    # editorial = models.CharField(max_length=200, null=True, blank=True)
    # editorial_city = models.CharField(max_length=50, null=True, blank=True)
    # publish_date = models.IntegerField(max_length=4, null=True, blank=True)
    # collection = models.CharField(max_length=100, null=True, blank=True)
    # description = models.TextField(max_length=300, null=True, blank=True)
    # upload_file = models.FileField(null=True, blank=True, upload_to='')
    class Meta:
        model = Book
        fields = ['book_name', 'author1', 'author2', 'editorial']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['book_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter book name'})
        self.filters['author1'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter first author name'})
        self.filters['author2'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter second author name'})
        self.filters['editorial'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter editorial company'})
        self.filters['editorial_city'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter the city where the book was printed'})
        self.filters['publish_date'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter the year of the printing'})
        self.filters['collection'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter the collection\'s name'})


