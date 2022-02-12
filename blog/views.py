from django.shortcuts import render
from .models import Post


def home(request):
    content = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blogs/home.html', content)


def about(request):
    return render(request, 'blogs/about.html', {'title': 'About'})