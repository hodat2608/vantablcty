from django.contrib import admin
from .models import PostViews, CommentViews, ProfileUser,Repply_commentviews

admin.site.register(PostViews)
admin.site.register(CommentViews)
admin.site.register(ProfileUser)
admin.site.register(Repply_commentviews)