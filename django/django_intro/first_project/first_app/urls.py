from django.urls import path
from . import views
urlpatterns = [
    path('p', views.index),
    path('p/new',views.new),
    path('p/create',views.create),
    path('p/<number>',views.show),
    path('p/<number>/edit',views.edit),
    path('p/<number>/delete',views.destroy)
]