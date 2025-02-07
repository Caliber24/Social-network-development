from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    class Status(models.IntegerChoices):
        ACTIVE = '1', "ACTIVE"
        DISABLE = '0', "DISABLE"
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.PositiveSmallIntegerField(
        default=0, choices=Status.choices)

    def __str__(self):
        return self.title + " - " + self.author.email
    def get_react_count(self):
        return React.objects.filter(post=self).count()
    def get_like_count(self):
        return React.objects.filter(post=self, is_like=True).count()
    def get_dislike_count(self):
        return React.objects.filter(post=self, is_like=False).count()


class React(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reacts')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='reacts')
    is_like = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'post')
