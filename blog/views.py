from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

Post.objects.get(pk=pk)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
