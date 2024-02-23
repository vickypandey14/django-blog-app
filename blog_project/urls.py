from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', home, name='home'),
    path('author/', include('author.urls')),
    path('profiles/', include('profiles.urls')),
    path('category/', include('category.urls')),
    path('post/', include('post.urls')),
    path('musicians_directory/', include('musicians_directory.urls')),

]
