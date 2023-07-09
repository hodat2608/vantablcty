from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse 
from .models import PostViews, CommentViews , User, ProfileUser
from django.shortcuts import get_object_or_404, render
from .forms import user_post_form,user_send_comment_form
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


def homepage(request,):
    posts = PostViews.objects.all()
    context = {'posts' : posts,}
    return render(request, 'homepage.html', context)

def post_likes_homepage(request,pk):
    post = PostViews.objects.get(pk=pk)
    user = request.user
    if request.method == 'POST':
        if user in post.post_likes.all():
            post.post_likes.remove(user)
        else:
            post.post_likes.add(user)
    return redirect('homepage')

def profile_post(request,pk):
    all_posts = PostViews.objects.filter(post_user_id=pk)
    profile_user_id = ProfileUser.objects.get(user_id=pk) 
    context = {'all_posts' : all_posts,'profile_user_id':profile_user_id }
    return render(request, 'vantablack_html/profile_post.html', context)

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

def post_comment_section(request,pk):
    post_comment_section_id = get_object_or_404(PostViews,pk=pk)
    return render(request, 'vantablack_html/post_&_comment_section.html', {'post_comment_section_id' : post_comment_section_id},)


def post_like_post_comment_section(request,pk):
    post_like_post_comment_section_id = get_object_or_404(PostViews,pk=pk)
    user = request.user
    if request.method == 'POST':
        if user in post_like_post_comment_section_id.post_likes.all():
            post_like_post_comment_section_id.post_likes.remove(user)
        else:
            post_like_post_comment_section_id.post_likes.add(user)
    return redirect('post_comment_section',post_like_post_comment_section_id.id)


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


def search_user(request):
    posts = PostViews.objects.all()
    if request.method == 'GET':
        query =  request.GET.get('query')  
        if query :
            try:
                search_users = User.objects.filter(username__icontains=query)
                context = {'search_users': search_users,'posts':posts}
            except User.DoesNotExist:
                return render(request, 'homepage.html', {
                    'error': "Không tìm thấy kết quả",
                })
        else:
            context = {'posts': posts} 
        return render(request, 'homepage.html', context)


def send_comment(request,pk):
    comment_for_post = get_object_or_404(PostViews,pk=pk)
    comment_for_post_where_id = comment_for_post.id
    if request.method == 'POST':
        form = user_send_comment_form(request.POST, request.FILES)
        if form.is_valid():
            message = form.cleaned_data['message']
            massage_image = request.FILES.get('massage_image')
            send_message = CommentViews.objects.create(comment_user=request.user,post_comment=comment_for_post,
                message=message,massage_image=massage_image)
            send_message.save()
            return redirect('post_comment_section',pk=comment_for_post_where_id)
    else: 
        form = user_send_comment_form()
    return render(request, 'reddot_html/post_&_comment_section.html', {'form' : form},)

def del_comment(request,pk):
    del_comment_id = CommentViews.objects.get(pk=pk)
    del_comment_id.delete()
    del_comment_of_post = del_comment_id.post_comment_id
    return redirect('post_comment_section',del_comment_of_post)


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