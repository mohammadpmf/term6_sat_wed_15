from django.shortcuts import render, redirect
from .models import BlogPost

def show_all_posts(request):
    context = {'posts': BlogPost.objects.filter(status='p')}
    return render(request, 'posts_list.html', context)

def show_detail(request, pk):
    context = {'post': BlogPost.objects.get(pk=pk)}
    return render(request, 'post_detail.html', context)

from .forms import BlogPostForm
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
            form.save()
            return redirect("blog")
    form = BlogPostForm()
    return render(request, 'post_new.html', {'form': form})

