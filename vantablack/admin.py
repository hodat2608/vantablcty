from django.contrib import admin
from .models import PostViews, CommentViews, ProfileUser,activity_history

admin.site.register(PostViews)
admin.site.register(CommentViews)
admin.site.register(ProfileUser)
admin.site.register(activity_history)