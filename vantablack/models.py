from django.db import models

from django.db import models
from django.contrib.auth.models import User


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    full_name = models.CharField(max_length=20, null=True, blank= True )
    avatar = models.ImageField(upload_to='images/', null=True,blank=True)
    bio = models.TextField(null=True, blank= True)
    date_birth = models.DateField(null=True,blank= True)
    email = models.EmailField(unique=True, null=True)
    address = models.TextField(null=True, blank= True, max_length=1000000)
    phone_number = models.TextField(null=True, blank= True, max_length=1000000)
    date_join = models.DateTimeField(auto_now_add=True)
    def __str__(self):

        return self.user.username


class PostViews(models.Model):
    post_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    discription =  models.TextField(max_length=1000000, blank=True,null=True)
    post_image = models.ImageField(upload_to='images/', null=True,blank=True)
    post_likes = models.ManyToManyField(User, related_name='post_likes',blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.discription
    
#repply for post??
class CommentViews(models.Model):
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post_comment = models.ForeignKey(PostViews, on_delete=models.CASCADE, null=True)
    message = models.TextField(max_length=1000000,blank=True,null=True)
    massage_image = models.ImageField(upload_to='images/', null=True,blank=True)
    comment_likes = models.ManyToManyField(User, related_name='comment_likes',blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.comment_user.username
    
#repply for comment?
class Repply_commentviews(models.Model):
    user_rep = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    rep_commentviews = models.ForeignKey(CommentViews, on_delete=models.CASCADE, null=True)
    rep_message = models.TextField(max_length=1000000,null=True,blank=True)
    rep_mess_image = models.ImageField(upload_to='images/', null=True,blank=True)
    rep_comment_likes = models.ManyToManyField(User, related_name='rep_comment_likes',blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.rep_message



#history_activity
class liked_post_activity(models.Model):
    user_liked_activity = models.ForeignKey(User, on_delete=models.CASCADE)
    post_liked_activity = models.ForeignKey(PostViews, on_delete=models.CASCADE, null=True,blank=True)
    activity_emotion = models.CharField(max_length=20,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.post_liked_activity
    

class commented_post_activity(models.Model):
    user_comment_activity = models.ForeignKey(User, on_delete=models.CASCADE)
    post_comment_activity = models.ForeignKey(PostViews, on_delete=models.CASCADE,null=True,blank=True)
    comment_content = models.ForeignKey(CommentViews,on_delete=models.CASCADE,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.post_comment_activity
    

class liked_comment_activity(models.Model):
    user_liked_comment = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    comment_liked_activity = models.ForeignKey(CommentViews,on_delete=models.CASCADE,null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.comment_liked_activity
    
class repply_comment_activity(models.Model):
    user_rep_comment = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    comment_rep_activity = models.ForeignKey(CommentViews,on_delete=models.CASCADE,null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.comment_rep_activity

    


