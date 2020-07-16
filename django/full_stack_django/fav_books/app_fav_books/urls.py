from django.urls import path
from . import views	

urlpatterns = [
    path('',views.index),
    path('createUser',views.create_user),
    path('login',views.login),
    path('books',views.home),
    path('addFavorite/<int:id>',views.add_favorite),
    path('unFavorite/<int:id>',views.unfavorite),
    path('addBook',views.add_book),
    path('books/<int:id>',views.some_book),
    path('all',views.all),
    path('destroy',views.log_out),
    path('deleteUser/<int:id>',views.delete_user),
    path('deleteBook/<int:id>',views.delete_book),
    path('favoriteBooks',views.favorite_books),
    path('books/<int:id>/edit',views.edit_book)
]