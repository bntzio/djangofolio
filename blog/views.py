from django.shortcuts import render, get_object_or_404

from .models import Blog

def posts(request):
    all_posts = Blog.objects
    return render(request, 'blog/posts.html', {'posts':all_posts})

def post(request, post_id):
    blog_post = get_object_or_404(Blog, pk=post_id)
    return render(request, 'blog/post.html', {'post':blog_post})
