from django.urls import path

from twitter import views

urlpatterns = [
    path('', views.twitter, name='twitter'),
]
