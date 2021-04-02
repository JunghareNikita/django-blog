from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm, SignupForm
from .models import BlogsModel
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout

def home(request):
    blog = BlogsModel.objects.all()
    return render(request, 'blog/home.html', {'blog':blog})

def UserSignup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
            return redirect('/')
    else:
         form = SignupForm()
    return render(request, 'blog/signup.html', {'form': form})

@login_required()
def dashboard(request):
    user = User.objects.filter(username=request.user, groups__name='Admin')
    if user:
        blog = BlogsModel.objects.all()
    else:
        blog = BlogsModel.objects.filter(user=request.user)
    return render(request, 'blog/dashboard.html', {'blogs':blog})


@login_required()
def profile(request, pk):
    user = User.objects.get(id=pk)
    form = SignupForm(instance=user)
    if request.method == "POST":
        form = SignupForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        return render(request, 'blog/profile_update.html', {'form': form})
    return render(request, 'blog/profile_update.html', {'form': form})


@login_required()
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required()
def BlogAdd(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        form.save()
        return redirect('dashboard')
    else:
        form = BlogForm()
    return render(request, 'blog/blog_add.html', {'form':form})

@login_required()
def BlogEdit(request, pk):
    user = BlogsModel.objects.get(id=pk)
    form = BlogForm(instance=user)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return render(request, 'blog/blog_add.html', {'form':form})


def AdminSinup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Admin')
            user.groups.add(group)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'blog/admin_signup.html', {'form':form})

@login_required()
def BlogDelete(request, pk):
    if request:
        blog = BlogsModel.objects.get(id=pk)
        blog.delete()
        return redirect('dashboard')
