# profiles/urls.py
from django.urls import path
from .views import category

urlpatterns = [
    path('', category, name='category'),
    # Add other category-related URL patterns if needed
]
