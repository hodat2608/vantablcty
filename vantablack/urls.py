from django.urls import path
from django.http import HttpResponse 
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name= 'homepage'),
    path('post_likes_homepage/<str:pk>/', views.post_likes_homepage, name = 'post_likes_homepage'),
    path('post_profile/<str:pk>/', views.profile_post, name = 'post_profile'),
    path('create_post/', views.create_post, name = 'create_post'),
    path('del_post/<str:pk>/', views.del_post, name = 'del_post'),
    path('del_comment/<str:pk>/', views.del_comment, name = 'del_comment'),
    path('post_likes_post_profile/<str:pk>/', views.post_likes_post_profile, name = 'post_likes_post_profile'),
    path('sare_post_likes/<str:pk>/', views.sare_post_likes, name = 'sare_post_likes'),
    path('update_post_likes/<str:pk>/', views.update_post_likes, name = 'update_post_likes'),
    path('sare_post_likes_section/<str:pk>/', views.sare_post_likes_section, name = 'sare_post_likes_section'),
    path('post_like_post_comment_section/<str:pk>/', views.post_like_post_comment_section, name = 'post_like_post_comment_section'),
    path('send_comment/<str:pk>/', views.send_comment, name = 'send_comment'),
    path('repply_comment/<str:pk>/', views.repply_comment, name = 'repply_comment'),
    path('share_post_views/<str:pk>/', views.share_post_views, name = 'share_post_views'),
    path('search_user/', views.search_user, name = 'search_user'),
    path('user_signup/', views.user_signup, name='user_signup'),
    path('', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
]

 