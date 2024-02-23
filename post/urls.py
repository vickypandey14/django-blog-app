# profiles/urls.py
from django.urls import path
from .views import post
from . import views

urlpatterns = [
    path('', post, name='post'),
        path('edit/<int:id>', views.edit_post, name='edit_post'),
    path('delete/<int:id>', views.delete_post, name='delete_post'),
    # Add other post-related URL patterns if needed
]
