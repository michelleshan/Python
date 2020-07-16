from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('shows',views.index),
    path('shows/new',views.add_show),
    path('shows/createShow',views.shows_create),
    path('shows/<int:id>',views.show_info),
    path('shows/<int:id>/edit',views.edit_show),
    path('shows/<int:id>/update',views.shows_update),
    path('shows/<int:id>/destroy',views.delete_show)
]