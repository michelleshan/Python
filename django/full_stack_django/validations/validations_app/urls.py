from django.urls import path
from . import views

urlpatterns = [
    path('', views.update),
    path('blog/edit/<int:id>',views.edit),
    path('blogs',views.blogs)
]