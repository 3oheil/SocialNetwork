from django.db import models

from django.conf import settings


class Post(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    caption = models.CharField(max_length=512)
    is_active = models.BooleanField(default=True)
    is_public = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'


class PostFile(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.FileField()
    create_date = models.DateTimeField(auto_now_add=True)
    upload_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = 'post file'
        verbose_name_plural = 'post files'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    is_approved = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class Like(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.PROTECT, related_name='likes')
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = 'like'
        verbose_name_plural = 'likes'
