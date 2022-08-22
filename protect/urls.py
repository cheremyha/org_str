"""
Let`s create url to which the user is redirected
after successfully logging in to the site.
In this case, it`s the root page of the site ('').
"""
from django.urls import path
from .views import RootPageView

urlpatterns = [
    path('', RootPageView.as_view()),
]