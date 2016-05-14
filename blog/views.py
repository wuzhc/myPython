from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .models import Post
from .forms import PostForm

#博客列表
def post_list(request):
    posts = Post.objects.filter(published_date__isnull = False).order_by("-create_date")
    #posts = Post.objects.order_by("-create_date")
    return render(request, 'blog/post_list.html', {'posts':posts})

#博客详情
def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

#创建博客
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) #参数commit，赋值为False，代表不要提交到数据库
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form':form})

#编辑博客
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_new.html', {'form':form})

#发布博客
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog:post_detail', pk=post.pk)

#未发布博客列表
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull = True).order_by("-create_date")
    return render(request, 'blog/post_draft_list.html', {'posts':posts})

#删除博客
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog:post_list')