from django.db import models

from django.db import models
from django.contrib.auth.models import User


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    full_name = models.CharField(max_length=20, null=True, blank= True )
    avatar = models.ImageField(upload_to='images/', null=True,blank=True)
    bio = models.TextField(null=True, blank= True)
    date_birth = models.DateField(null=True)
    email = models.EmailField(unique=True, null=True)
    address = models.TextField(null=True, blank= True, max_length=1000000)
    phone_number = models.TextField(null=True, blank= True, max_length=1000000)
    date_join = models.DateTimeField(auto_now_add=True)
    def __str__(self):

        return self.user.username


class PostViews(models.Model):
    post_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    discription =  models.TextField(null=True,max_length=1000000, blank= True)
    post_image = models.ImageField(upload_to='images/', null=True,blank=True)
    post_likes = models.ManyToManyField(User, related_name='post_likes')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.discription
    

class CommentViews(models.Model):
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post_comment = models.ForeignKey(PostViews, on_delete=models.CASCADE, null=True)
    message = models.TextField(null=False, max_length=1000000,blank= True)
    massage_image = models.ImageField(upload_to='images/', null=True,blank=True)
    comment_likes = models.ManyToManyField(User, related_name='comment_likes')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.comment_user.username


class activity_history(models.Model):
    activity_user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_post = models.ForeignKey(PostViews, on_delete=models.CASCADE, null=True,blank=True)
    activity_comment = models.ForeignKey(CommentViews, on_delete=models.CASCADE, null=True,blank=True)
    activity_action = models.CharField(max_length=20)
    shared_to_profile = models.BooleanField(default=False,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.activity_action