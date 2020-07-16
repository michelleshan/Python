from django.urls import path
from . import views	

urlpatterns = [
    path('', views.index),
    path('users', views.createUser),
    path('login', views.login),
    path('homepage', views.homepage),
    path('cats', views.createCat),
    path('deleteCat/<int:id>',views.deleteCat),
    path('voteCat/<int:id>',views.voteCat),
    path('unvoteCat/<int:id>',views.unvoteCat),
    path('profile',views.userProfile),
    path('cat/<int:id>',views.catProfile)
]