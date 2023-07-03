from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse 
from .models import PostViews, CommentViews , User
from django.shortcuts import get_object_or_404, render
from .forms import user_post_form
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import  HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.shortcuts import render
import csv
from django.db.models import Q
from django.http import JsonResponse

def profile_post(request,pk):
    all_posts = PostViews.objects.filter(post_user_id=pk)
    context = {'all_posts' : all_posts, }
    return render(request, 'vantablack_html/profile_post.html', context)

def homepage(request,):
    posts = PostViews.objects.all()
    context = {'posts' : posts,}
    return render(request, 'homepage.html', context)

def create_post(request):
    if request.method == 'POST':
        form = user_post_form(request.POST, request.FILES)
        if form.is_valid():
            discription = form.cleaned_data['discription']
            post_image = request.FILES['post_image']
            createpost = PostViews.objects.create(post_user=request.user,discription=discription,post_image=post_image,)
            createpost.save()
            return redirect('homepage')
    else: 
        form = user_post_form()
    return render(request, 'vantablack_html/create_post.html', {'form': form})

def del_post(request,pk):
    del_post = get_object_or_404(PostViews,pk=pk)
    del_post.delete()
    return redirect('post_profile',del_post.post_user_id)

def post_likes_homepage(request,pk):
    post = PostViews.objects.get(pk=pk)
    user = request.user
    if request.method == 'POST':
        if user in post.post_likes.all():
            post.post_likes.remove(user)
        else:
            post.post_likes.add(user)
    return redirect('homepage')

def post_likes_post_profile(request,pk):
    post = PostViews.objects.get(pk=pk)
    post_user = post.post_user_id
    user = request.user
    if request.method == 'POST':
        if user in post.post_likes.all():
            post.post_likes.remove(user)
        else:
            post.post_likes.add(user)
    return redirect('post_profile',pk=post_user)

def search_user(request):
    if request.method == 'GET':
        query =  request.GET.get('query')  
        if query :
            try:
                search_users = User.objects.filter(username__icontains=query)
                context = {'search_users': search_users}
            except User.DoesNotExist:
                return render(request, 'homepage.html', {
                    'error2': "Không tìm thấy",
                })
        else:
            context = {} 
        return render(request, 'vantablack_html/search_user.html', context)

def post_comment_section(request,pk):
    post_comment_section_id = get_object_or_404(PostViews,pk=pk)
    user = request.user
    if request.method == 'POST':
        if user in post_comment_section_id.post_likes.all():
            post_comment_section_id.post_likes.remove(user)
        else:
            post_comment_section_id.post_likes.add(user)
    return render(request, 'vantablack_html/post_&_comment_section.html', {'post_comment_section_id' : post_comment_section_id},)

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Form1:List_nhan_vien')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            request.session['username'] = user.username
            return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    del request.session['username']
    auth_logout(request)
    return redirect('vantablack_html:user_login')
