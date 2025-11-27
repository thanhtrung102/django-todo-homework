from django.contrib import admin
from django.urls import path, include  # <--- 1. Make sure 'include' is imported here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_app.urls')), # <--- 2. Add this line
]