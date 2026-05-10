from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Blog, Comment, Category


def main(request):
    return render(request, 'blog/main.html')


def users(request):
    users = User.objects.all()
    return render(request, 'blog/users.html', {'users': users})


def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blogs.html', {'blogs': blogs})


def comments(request):
    comments = Comment.objects.all()
    return render(request, 'blog/comments.html', {'comments': comments})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'blog/categories.html', {'categories': categories})


def blogdetails(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'blog/blogdetails.html', {'blog': blog})