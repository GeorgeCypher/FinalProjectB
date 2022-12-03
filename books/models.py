from django.db import models

class Book(models.Model):

    # gender_options = (('male', 'Male'), ('female', 'Female'))

    book_name = models.CharField(max_length=100, null=True, blank=True)
    author1 = models.CharField(max_length=100, null=True, blank=True)
    author2 = models.CharField(max_length=100, null=True, blank=True)
    editorial = models.CharField(max_length=200, null=True, blank=True)
    editorial_city = models.CharField(max_length=50, null=True, blank=True)
    publish_date = models.IntegerField(max_length=4, null=True, blank=True)
    collection = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=300, null=True, blank=True)
    upload_file = models.FileField(null=True, blank=True, upload_to='')
    # # needs to add attachments of cover and of pdf
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.book_name} by {self.author1}'
# Create your models here.
