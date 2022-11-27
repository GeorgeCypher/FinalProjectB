from django.urls import path

from books import views

urlpatterns = [
    path('add-book/', views.BookCreateView.as_view(), name='add_book'),
    path('list-of-books/', views.BookListView.as_view(), name='list_of_books'),
    path('update-book/<int:pk>/', views.BookUpdateView.as_view(), name='update_book'),
    path('delete-book/<int:pk>/', views.BookDeleteView.as_view(), name='delete_book'),
    path('delete-book-by-modal/<int:pk>/', views.delete_book_by_modal, name='delete_book_by_modal'),
    path('details-book/<int:pk>', views.BookDetailView.as_view(), name='details_book')

    # path('books/upload/', views.upload_book, name='upload_book'),
    # path('books/<int:pk>/', views.delete_book, name='delete_book'),
    #
    # path('class/books/', views.BookListView.as_view(), name='class_book_list'),
    # path('class/books/upload/', views.UploadBookView.as_view(), name='class_upload_book'),

]