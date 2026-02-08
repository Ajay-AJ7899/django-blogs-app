from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

# Blog list page
def post_list(request):
    posts = [
        {"title": "blog1","content":"first blog"},
    ]
    posts = Post.objects.all().order_by('-created_date')
    return render(request, 'blogsapp/post_list.html', {'posts': posts})
    # return render(request, 'blogsapp/post_list.html', {'posts': posts})

# Single blog detail
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blogsapp/post_detail.html', {'post': post})
