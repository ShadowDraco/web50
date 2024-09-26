from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    watching = models.ManyToManyField("User", related_name="following")
    liked_posts = models.ManyToManyField("Post", related_name='likes')
    
    def getFollowingCount (self):
        return len(self.watching)

class Post(models.Model):
    posted_by = models.ForeignKey("User", on_delete=models.CASCADE, related_name="poster", null=True)
    poster_name = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)

    def getLikeCount (self):
        return len(self.likes)
