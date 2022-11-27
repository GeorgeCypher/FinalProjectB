from django import forms
from django.forms import TextInput, Select, Textarea, DateInput, BooleanField, FileInput
from django.forms.widgets import CheckboxInput, NumberInput
from books.models import Book
from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

class BookForm(forms.ModelForm):
    file= forms.FileField
    class Meta:
        model = Book
        fields = ['book_name', 'author1', 'author2', 'editorial', 'editorial_city', 'publish_date', 'collection',
                  'description', 'upload_file']

        # fields = ['book_name', 'author1', 'author2', 'editorial', 'editorial_city', 'publish_date',
        #           'publish_date', 'collection', 'needs_details', 'description']
        widgets = {
            'book_name': TextInput(attrs={'placeholder': 'Place title of book', 'class': 'form-control'}),
            'author1': TextInput(attrs={'placeholder': 'Enter name of author', 'class': 'form-control'}),
            'author2': TextInput(
                attrs={'placeholder': 'Enter name of other author (if it has another)', 'class': 'form-control'}),
            'editorial': TextInput(attrs={'placeholder': 'Enter the editorial company name', 'class': 'form-control'}),
            'editorial_city': TextInput(
                attrs={'placeholder': 'Add the city of the company (if known)', 'class': 'form-control'}),
            'publish_date': NumberInput(attrs={'placeholder': 'year', 'class': 'form-control', 'type': 'number'}),
            'collection': TextInput(attrs={'placeholder': 'Insert collection name', 'class': 'form_control'}),
            'description': Textarea(
                attrs={'placeholder': 'Please enter your description', 'class': 'form-control', 'rows': 4}),
            'upload_file': FileInput()
        }

    # needs to add attachments of cover and of pdf
    def clean(self):
        cleaned_data = self.cleaned_data
        booknamecheck = cleaned_data.get('book_name')
        if booknamecheck[0].islower():
            msg = 'First letter cannot be lower'
            self._errors['booknamecheck'] = self.error_class([msg])

        author1check = cleaned_data.get('author1')
        if author1check[0].islower():
            msg = 'First letter cannot be lower'
            self._errors['author1check'] = self.error_class([msg])

        # author2check = cleaned_data.get('author2')
        # if author2check[0].islower():
        #     msg = 'First letter cannot be lower'
        #     self._errors['author2check'] = self.error_class([msg])
        #
        # publishcheck = cleaned_data.get('publish_date')
        # has_publish_date = cleaned_data.get('has_publish_date')
        # if has_publish_date is True and publishcheck[0].islower():
        #     msg = 'Mush add date if you toggled publish date'
        #     self._errors['last_name'] = self.error_class([msg])

        return cleaned_data


class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_name', 'author1', 'author2', 'editorial', 'editorial_city', 'publish_date', 'collection',
                  'description', 'upload_file']

        # fields = ['book_name', 'author1', 'author2', 'editorial', 'editorial_city', 'publish_date',
        #           'publish_date', 'collection', 'needs_details', 'description']
        widgets = {
            'book_name': TextInput(attrs={'placeholder': 'Place title of book', 'class': 'form-control'}),
            'author1': TextInput(attrs={'placeholder': 'Enter name of author', 'class': 'form-control'}),
            'author2': TextInput(
                attrs={'placeholder': 'Enter name of other author (if it has another)', 'class': 'form-control'}),
            'editorial': TextInput(attrs={'placeholder': 'Enter the editorial company name', 'class': 'form-control'}),
            'editorial_city': TextInput(
                attrs={'placeholder': 'Add the city of the company (if known)', 'class': 'form-control'}),
            'publish_date': NumberInput(attrs={'placeholder': 'year', 'class': 'form-control', 'type': 'number'}),
            'collection': TextInput(attrs={'placeholder': 'Insert collection name', 'class': 'form_control'}),
            'description': Textarea(
                attrs={'placeholder': 'Please enter your description', 'class': 'form-control', 'rows': 4}),
            'upload_file': FileInput()

        }
        # fields = ['book_name', 'author1', 'author2', 'editorial', 'editorial_city', 'publish_date',
        #           'publish_date', 'collection', 'needs_details', 'description']
        # widgets = {
        #     'book_name': TextInput(attrs={'placeholder': 'Place title of book', 'class': 'form-control'}),
        #     'author1': TextInput(attrs={'placeholder': 'Enter name of author', 'class': 'form-control'}),
        #     'author2': TextInput(
        #         attrs={'placeholder': 'Enter name of other author (if it has another)', 'class': 'form-control'}),
        #     'editorial': TextInput(attrs={'placeholder': 'Enter the editorial company name', 'class': 'form-control'}),
        #     'editorial_city': TextInput(
        #         attrs={'placeholder': 'Add the city of the company (if known)', 'class': 'form-control'}),
        #     'publish_date': TextInput(attrs={'placeholder': 'year', 'class': 'form-control', 'type': 'year'}),
        #     'collection': TextInput(attrs={'placeholder': 'Insert collection name', 'class': 'form_control'}),
        #     'needs_details': Select(attrs={'class': 'form-select'}),
        #     'description': Textarea(
        #         attrs={'placeholder': 'Please enter your description', 'class': 'form-control', 'rows': 4})
        #
        # }

    # needs to add attachments of cover and of pdf
    def clean(self):
        cleaned_data = self.cleaned_data

        # if cleaned_data.get('publish_date') > cleaned_data.get('created_at') or cleaned_data.get(
        #         'publish_date') > cleaned_data.get('updated_at'):
        #     msg = 'Publish date is impossible'
        #     self._errors['start_date'] = self.error_class([msg])

        booknamecheck = cleaned_data.get('book_name')
        if booknamecheck[0].islower():
            msg = 'First letter cannot be lower'
            self._errors['booknamecheck'] = self.error_class([msg])

        author1check = cleaned_data.get('author1')
        if author1check[0].islower():
            msg = 'First letter cannot be lower'
            self._errors['author1check'] = self.error_class([msg])

        # author2check = cleaned_data.get('author2')
        # if author2check[0].islower():
        #     msg = 'First letter cannot be lower'
        #     self._errors['author2check'] = self.error_class([msg])
        #
        # publishcheck = cleaned_data.get('publish_date')
        # has_publish_date = cleaned_data.get('has_publish_date')
        # if has_publish_date is True and publishcheck[0].islower():
        #     msg = 'Mush add date if you toggled publish date'
        #     self._errors['last_name'] = self.error_class([msg])

        return cleaned_data
