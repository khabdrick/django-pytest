from django.contrib import admin
from django.urls import path
from blog.views import post_content

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:pk>',post_content, name="content")
]
