from django.shortcuts import render, redirect
from .models import Post
from .forms import Postform, Userregister
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm


def index(request):
    posts = Post.objects.all()
    myform = Postform()
    if request.method == 'POST':
        myform = Postform(request.POST)
        if myform.is_valid:
            myform.save()
        return redirect('/')

    context = {'posts': posts, 'myform': myform}
    return render(request, 'index.html', context)

def update(request, pk):
    posts = Post.objects.get(id=pk)
    myform = Postform(instance=posts)
    if request.method == 'POST':
        myform = Postform(request.POST, instance=posts)
        if myform.is_valid:
            myform.save()
        return redirect('/')

    context = {'posts': posts, 'myform': myform}
    return render(request, 'update.html', context)

def delete(request, pk):
    posts = Post.objects.get(id=pk)

    if request.method == 'POST':
        posts.delete()
        return redirect('/')
  
    context = {'posts': posts}
    return render(request, 'delete.html', context)



    