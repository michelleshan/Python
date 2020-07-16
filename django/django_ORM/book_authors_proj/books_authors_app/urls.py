from django.urls import path
from . import views

urlpatterns = [
    path('',views.main),
    path('books_index',views.books_index),
    path('books/<int:id>',views.books),
    path('add_missing_author/<int:id>',views.add_missing_author),
    path('delete_author/<int:id>/<int:author_id>',views.delete_author),
    path('add_books',views.add_books),
    path('return_main',views.return_main),
    path('authors_index',views.authors_index),
    path('authors/<int:id>',views.authors),
    path('add_missing_book/<int:id>',views.add_missing_book),
    path('add_authors',views.add_authors),
    path('return_authors_index',views.return_authors_index),
    path('delete_book/<int:id>/<int:book_id>',views.delete_book)
]