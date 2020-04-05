from django.shortcuts import render
from .models import Post

# Dummy Data
# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post comment',
#         'date_posted': 'April 4, 2020'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post comment',
#         'date_posted': 'April 5, 2020'
#     }
# ]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'});