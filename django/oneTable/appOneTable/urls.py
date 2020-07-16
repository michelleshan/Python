from django.urls import path
from . import views

urlpatterns = [
    path('',views.firstFunction),
    path('register_dungeon',views.register_dungeon),
    path('register_prisoner',views.register_prisoner),
    path('delete/<int:id>',views.delete)
]