from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index),
    path('random_word',views.random_word),
    path('delete_session',views.delete_session)
]