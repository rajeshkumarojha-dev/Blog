from django.shortcuts import render,get_object_or_404,redirect
from app1.models import Blog
from app1.forms import BlogForm,registerForm,LoginForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    qs=Blog.objects.all()
    return render(request,'app1/index.html',context={'qs':qs})

@login_required
def createBlog(request):
    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES)
        if form.is_valid():
           tweet= form.save(commit=False)
           tweet.user=request.user
           tweet.save()
           return redirect('home')
    else:
        form=BlogForm()
    return render(request,'app1/create.html',context={'form':form})

@login_required
def editBlog(request,id):
    tweet=Blog.objects.get(pk=id,user=request.user)
    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('home')
    else:
        form=BlogForm(instance=tweet)
    return render(request,'app1/update.html',context={'form':form})

@login_required
def deleteBlog(request,id):
    tweet=get_object_or_404(Blog,pk=id,user=request.user)
    tweet.delete()
    return redirect('home')

def register_request(request):
    if request.method=='POST':
        form=registerForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')
    else:
        form=registerForm()
    return render(request,'registration/register.html',context={'form':form})

def login_request(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get('username')
            upass=form.cleaned_data.get('password')
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        form=LoginForm()
    return render(request,'registration/login.html',context={'form':form})

def logout_request(request):
    logout(request)
    return redirect('home')