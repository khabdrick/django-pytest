from django.shortcuts import get_object_or_404, render
from .models import Post

def blog_content(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog_contet.html", {'post':post})