from django.shortcuts import render
from django.http import HttpResponse 
from .models import PostViews, CommentViews , User, ProfileUser,Repply_commentviews,share_post
from django.shortcuts import get_object_or_404, render
from .forms import user_post_form,user_send_comment_form,repply_comment_form
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

@login_required(login_url='user_login')
def homepage(request,):
    posts = PostViews.objects.all()
    context = {'posts' : posts,}
    return render(request, 'homepage.html', context)

@login_required(login_url='user_login')
def post_likes_homepage(request,pk):
    post = PostViews.objects.get(pk=pk)
    user = request.user
    if request.method == 'POST':
        if user in post.post_likes.all():
            post.post_likes.remove(user)
            liked = False
        else:
            post.post_likes.add(user)
            liked = True
    likes_count = post.post_likes.count()
    all_user_like = list(post.post_likes.all().values_list('username', flat=True))
    context = {'liked':liked, 'likes_count':likes_count, 'all_user_like':all_user_like}
    return JsonResponse(context)

@login_required(login_url='user_login')
def profile_post(request,pk):
    all_posts = PostViews.objects.filter(post_user_id=pk)
    profile_user_id = ProfileUser.objects.get(user_id=pk) 
    share_key = share_post.objects.filter(user_share_post_id=pk)
    lst_id =[]
    for id in share_key:
        lst_id.append(id.share_post_id_id)
    post_id_share = PostViews.objects.filter(pk__in=lst_id)
    context = {'all_posts' : all_posts,'profile_user_id':profile_user_id,'share_key':share_key,'post_id_share':post_id_share}
    return render(request, 'vantablack_html/profile_post.html', context)

@login_required(login_url='user_login')
def post_likes_post_profile(request,pk):
    post = PostViews.objects.get(pk=pk)
    user = request.user
    if request.method == 'POST':
        if user in post.post_likes.all():
            post.post_likes.remove(user)
            liked = False
        else:
            post.post_likes.add(user)
            liked = True
    likes_count = post.post_likes.count()
    all_user_like = list(post.post_likes.all().values_list('username', flat=True))
    context = {'liked':liked, 'likes_count':likes_count, 'all_user_like':all_user_like}
    return JsonResponse(context)

def sare_post_likes(request,pk):
    item = get_object_or_404(share_post,pk=pk)
    user = request.user 
    if request.method =='POST':
        if user in item.share_post_likes.all():
            item.share_post_likes.remove(user)
            liked_sh_post = False
        else:
            item.share_post_likes.add(user)
            liked_sh_post=True
    likes_count_sh_post = item.share_post_likes.count()
    all_user_like = list(item.share_post_likes.all().values_list('username', flat=True))
    context={'liked_sh_post':liked_sh_post,'likes_count_sh_post':likes_count_sh_post,'all_user_like':all_user_like}
    return JsonResponse(context)

def sare_post_likes_section(request,pk):
    item = get_object_or_404(share_post,pk=pk)
    user = request.user 
    if request.method =='POST':
        if user in item.share_post_likes.all():
            item.share_post_likes.remove(user)
            liked_sh_post_section = False
        else:
            item.share_post_likes.add(user)
            liked_sh_post_section =  True
    likes_count_sh_post_section = item.share_post_likes.count()
    all_user_like = list(item.share_post_likes.all().values_list('username', flat=True))
    context={'liked_sh_post_section':liked_sh_post_section,'likes_count_sh_post_section':likes_count_sh_post_section,'all_user_like':all_user_like}
    return JsonResponse(context)

@login_required(login_url='user_login')
def post_comment_section(request,pk):
    post_comment_section_id = get_object_or_404(PostViews,pk=pk)
    return render(request, 'homepage.html', {'post_comment_section_id' : post_comment_section_id},)

@login_required(login_url='user_login')
def post_like_post_comment_section(request,pk):
    post_like_post_comment_section_id = get_object_or_404(PostViews,pk=pk)
    user = request.user
    if request.method == 'POST':
        if user in post_like_post_comment_section_id.post_likes.all():
            post_like_post_comment_section_id.post_likes.remove(user)
            liked_section = False
        else:
            post_like_post_comment_section_id.post_likes.add(user)
            liked_section = True 
    likes_count_section = post_like_post_comment_section_id.post_likes.count()
    context = {'liked_section':liked_section,'likes_count_section':likes_count_section}
    return JsonResponse(context)

def update_post_likes(request,pk):
    post_like_is = get_object_or_404(PostViews,pk=pk)
    user = request.user
    if request.method == 'POST':
        if user in post_like_is.post_likes.all():
            post_like_is.post_likes.remove(user)
            update_like = False
        else:
            update_like = True 
            post_like_is.post_likes.add(user)
    update_like_count = post_like_is.post_likes.count()
    context = {'update_like':update_like,'update_like_count':update_like_count}
    return JsonResponse(context)

@login_required(login_url='user_login')
def create_post(request):
    if request.method == 'POST':
        form = user_post_form(request.POST, request.FILES)
        if form.is_valid():
            discription = form.cleaned_data['discription']
            post_image = request.FILES.get('post_image')
            createpost = PostViews.objects.create(post_user=request.user,discription=discription,post_image=post_image,)
            createpost.save()
            return redirect('homepage')
    else: 
        form = user_post_form()
    return render(request, 'homepage.html', {'form': form})

@login_required(login_url='user_login') 
def del_post(request,pk):
    del_post = get_object_or_404(PostViews,pk=pk)
    del_post.delete()
    return redirect('post_profile',del_post.post_user_id)

@login_required(login_url='user_login')
def search_user(request):
    if request.method == 'GET':
        query = request.GET.get('query')  
        if query.strip() != '':
            search_users = User.objects.filter(username__icontains=query)
            #result = [{'username': user.username,'avatar':user.profileuser.avatar.url, 'profile_url': f'/post_profile/{user.id}/'} for user in search_users] 
            result = []
            for user in search_users:
                if hasattr(user, 'profileuser'):
                    avatar_url = user.profileuser.avatar.url
                else:
                    avatar_url = '/media/images/default_avatar.jpg'
                result.append({'username': user.username,'avatar':avatar_url,'profile_url': f'/post_profile/{user.id}/'}) #cách khác dễ hiểu hơn 
            return JsonResponse(result, safe=False)
        else:
            return JsonResponse([])
# end

@login_required(login_url='user_login')
def send_comment(request,pk):
    comment_for_post = get_object_or_404(PostViews,pk=pk)
    if request.method == 'POST':
        form = user_send_comment_form(request.POST, request.FILES)
        if form.is_valid():
            message = request.POST.get('message')
            massage_image = request.FILES.get('massage_image')
            send_message = CommentViews.objects.create(comment_user=request.user,post_comment=comment_for_post,
                message=message,massage_image=massage_image)
            send_message.save()
            avatar_url = send_message.get_comment_user_avatar().url if send_message.get_comment_user_avatar() else '/media/images/default_avatar.jpg'
            new_comment = { 
                'avatar_url': avatar_url,
                'user': request.user.username if request.user.is_authenticated else None,
                'profile_url': f'/post_profile/{send_message.comment_user_id}/',
                'comment_id': send_message.id,
                'comment_user_username': send_message.comment_user.username if send_message.comment_user else None,
                'comment_massage' : send_message.message,
                'comment_massage_image' : send_message.massage_image.url if send_message.massage_image else '',}              
            return JsonResponse(new_comment)
        else: 
            return JsonResponse({'error': 'sai form data'}, status=400)
    else: 
        form = user_send_comment_form()
    return render(request, 'homepage.html', {'form' : form},)


@login_required(login_url='user_login')
def del_comment(request,pk):
    del_comment_id = CommentViews.objects.get(pk=pk)
    if request.method == 'POST':
        del_comment_id.delete()
        id = del_comment_id.post_comment_id
        id_post = PostViews.objects.get(pk=id)
        commit = True
        print(commit) 
    return JsonResponse({'commit':commit})

def repply_comment(request,pk):
    comment_id = CommentViews.objects.get(pk=pk)
    if request.method == 'POST':
        form = repply_comment_form(request.POST, request.FILES)
        if form.is_valid():
            rep_message = request.POST.get('rep_message')
            rep_mess_image = request.FILES.get('rep_mess_image')
            repply_all = Repply_commentviews.objects.create(user_rep=request.user,rep_commentviews=comment_id,rep_message=rep_message,rep_mess_image=rep_mess_image)
            repply_all.save()
            avatar_url_rp = repply_all.get_repply_comment_user_avatar().url if repply_all.get_repply_comment_user_avatar() else '/media/images/default_avatar.jpg'
            new_repppy_cmt = {
                'avatar_url_rp': avatar_url_rp,
                'repply_id':repply_all.id,
                'profile_url_repply': f'/post_profile/{repply_all.user_rep_id}/',
                'repply_user_username':repply_all.user_rep.username,
                'repply_user_id':repply_all.user_rep.id,
                'repply_rep_message':repply_all.rep_message,
                'repply_rep_mess_image':repply_all.rep_mess_image.url if repply_all.rep_mess_image else " "}
            return JsonResponse(new_repppy_cmt)
    else:
        form = repply_comment_form()
    return render(request, 'homepage.html', {'form' : form},)

def share_post_views(request,pk):
    post_id = PostViews.objects.get(pk=pk)
    user = request.user
    if request.method == 'POST':
        if user in post_id.post_shares.all():
            boolean = False
        else:
            post_id.post_shares.add(user)
            discription_sh = request.POST.get('discription_sh')
            share_post_1 = share_post(user_share_post=request.user,share_post_id=post_id,discription_sh=discription_sh,) 
            share_post_1.save()
            boolean = True
    share_user_count = post_id.post_shares.count()
    all_user_share = list(post_id.post_shares.all().values_list('username', flat=True))
    context = {'boolean':boolean,'share_user_count':share_user_count,'all_user_share':all_user_share,}
    return JsonResponse(context)
            

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
