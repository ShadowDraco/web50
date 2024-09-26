from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    posts = models.ForeignKey("Post", on_delete=models.CASCADE, null=True)
    watching = models.ForeignKey("User", on_delete=models.CASCADE, related_name="following",  null=True)
    
    def getFollowingCount (self):
        return len(self.watching)

class Post(models.Model):
    posted_by = models.ForeignKey("User", on_delete=models.CASCADE, related_name="poster", null=True)
    liked_by = models.ForeignKey("User", on_delete=models.CASCADE, related_name="likes", null=True)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)

    def getLikeCount (self):
        return len(self.likes)
