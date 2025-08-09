from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.tweets/tweet_form, name='tweet_form'),

    path('success/', lambda request: render(request, 'tweets/tweet_list.html'), name='tweet_list'),
]