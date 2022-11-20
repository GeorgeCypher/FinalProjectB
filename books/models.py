from django.db import models

class Book(models.Model):

    # gender_options = (('male', 'Male'), ('female', 'Female'))

    book_name = models.CharField(max_length=100)
    author1 = models.CharField(max_length=100)
    author2 = models.CharField(max_length=100)
    editorial = models.CharField(max_length=200)
    editorial_city = models.CharField(max_length=50)
    has_publish_date = models.BooleanField(default=False)
    publish_date = models.DateField()
    is_collection = models.BooleanField(default=False)
    collection = models.CharField(max_length=100)
    needs_details = models.BooleanField(default=False)
    description = models.TextField(max_length=300)
    # needs to add attachments of cover and of pdf
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.book_name} by {self.author1}'
# Create your models here.
