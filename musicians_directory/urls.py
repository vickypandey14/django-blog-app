# musicians_directory/urls.py
from django.urls import path
from .views import musician_list, musician_create_or_update, musician_delete

urlpatterns = [
    path('musician/', musician_list, name='musician_list'),
    path('musician/create/', musician_create_or_update, name='musician_create_or_update'),
    path('musician/<int:musician_id>/', musician_create_or_update, name='musician_update'),
    path('musician/<int:musician_id>/delete/', musician_delete, name='musician_delete'),
]
