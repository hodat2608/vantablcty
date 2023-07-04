from django.contrib import admin
from .models import PostViews, CommentViews, ProfileUser

admin.site.register(PostViews)
admin.site.register(CommentViews)
admin.site.register(ProfileUser)