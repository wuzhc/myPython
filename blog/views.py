from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .models import Post
from .forms import PostForm

#�����б�
def post_list(request):
    posts = Post.objects.filter(published_date__isnull = False).order_by("-create_date")
    #posts = Post.objects.order_by("-create_date")
    return render(request, 'blog/post_list.html', {'posts':posts})

#��������
def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

#��������
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) #����commit����ֵΪFalse������Ҫ�ύ�����ݿ�
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form':form})

#�༭����
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

#��������
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog:post_detail', pk=post.pk)

#δ���������б�
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull = True).order_by("-create_date")
    return render(request, 'blog/post_draft_list.html', {'posts':posts})

#ɾ������
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog:post_list')