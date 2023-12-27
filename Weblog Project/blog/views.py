from django.shortcuts import render
from .models import BlogPost

def show_all_posts(request):
    context = {'posts': BlogPost.objects.filter(status='p')}
    return render(request, 'posts_list.html', context)

def show_detail(request, pk):
    context = {'post': BlogPost.objects.get(pk=pk)}
    return render(request, 'post_detail.html', context)
