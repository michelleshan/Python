from django.urls import path
from .  import views

urlpatterns = [
    path('', views.index),
    path('users', views.createUser),
    path('login', views.login),
    path('home', views.home),
    path('addquote', views.addQuote),
    path('delete/<int:id>', views.deleteQuote),
    path('delete2/<int:id>', views.deleteQuote2),
    path('like/<int:id>', views.Like),
    path('unlike/<int:id>', views.Unlike),
    path('myaccount', views.MyAccount),
    path('update', views.UpdateAccount),
    path('userquotes/<int:id>', views.UserQuotes),
    path('logout', views.logout),
]