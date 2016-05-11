from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__isnull = False)
    return render(request, 'blog/post_list.html', {'posts':posts})
