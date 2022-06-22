from django.shortcuts import render
from .models import Post
from .models import Paintings

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})



def post(request, pk):
    posts = Post.objects.get(id = pk)
    return render(request,'post.html',{'posts': posts})


def image(request, pk):
    images = Paintings.objects.all()
    return render(request, 'image.html', {'images': images})