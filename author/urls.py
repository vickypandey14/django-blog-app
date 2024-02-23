# author/urls.py
from django.urls import path
from .views import author_detail

urlpatterns = [
    path('', author_detail, name='author_detail'),
    # Add other author-related URL patterns if needed
]
