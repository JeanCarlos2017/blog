from django.shortcuts import render

from blog.models import Post



# Create your views here.


def home(request):
    posts = Post.objects.all
    return render(request, 'home.html', {'posts': posts})


def posts(request, post_id):
    dados={}
    dados['post'] = Post.objects.get(id=post_id)
    return render(request, 'post.html', dados)
