from django.urls import path
from django.http import HttpResponse 
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name= 'homepage'),
    path('post_profile/<str:pk>/', views.profile_post, name = 'post_profile'),
    path('create_post/', views.create_post, name = 'create_post'),
    path('del_post/<str:pk>/', views.del_post, name = 'del_post'),

    path('post_likes_homepage/<str:pk>/', views.post_likes_homepage, name = 'post_likes_homepage'),
    path('post_likes_post_profile/<str:pk>/', views.post_likes_post_profile, name = 'post_likes_post_profile'),

     path('post_comment_section/<str:pk>/', views.post_comment_section, name = 'post_comment_section'),

    path('search_user/', views.search_user, name = 'search_user'),

    path('user_signup/', views.user_signup, name='user_signup'),
    path('', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
]

