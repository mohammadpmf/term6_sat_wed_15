from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm

def show_all_posts(request):
    context = {'posts': BlogPost.objects.filter(status='p').order_by("-time_modified")}
    return render(request, 'posts_list.html', context)

def show_detail(request, pk):
    # context = {'post': BlogPost.objects.get(pk=pk)}
    context = {'post': get_object_or_404(BlogPost, pk=pk)}
    return render(request, 'post_detail.html', context)

def new_post(request):
    # if request.method=="POST":
    #     title = request.POST.get("title")
    #     text = request.POST.get("text")
    #     author = request.POST.get("author")
    #     status = request.POST.get("status")
    #     BlogPost.objects.create(title=title, text=text,
    #                             author=request.user, status=status)
    #     return redirect("blog")
    if request.method=="POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.author = request.user
            p.save()
            return redirect("blog")
    form = BlogPostForm()
    return render(request, 'post_new.html', {'form': form})

def update(request, pk):
    # post = BlogPost.objects.get(pk=pk)
    post=get_object_or_404(BlogPost, pk=pk)
    form = BlogPostForm(instance=post)
    return render(request, 'post_update.html', {'form': form})

def delete(request, pk):
    # post=BlogPost.objects.get(pk=pk)
    post=get_object_or_404(BlogPost, pk=pk)
    return render(request, 'post_delete.html', {'post': post})
