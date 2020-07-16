from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('success',views.success),
    path('createuser',views.create_user),
    path('login',views.login_user),
    path('allusers',views.all_users),
    path('delete/<int:id>',views.delete_users),
    path('destroy',views.destroy),
]