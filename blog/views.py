from django.shortcuts import get_object_or_404, render
from .models import Post


def post_content(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post_content.html", {'post':post})