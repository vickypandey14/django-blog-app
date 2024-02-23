from django.urls import path
from .views import profiles

urlpatterns = [
    path('', profiles, name='profiles'),
    # Add other profiles-related URL patterns if needed
]
