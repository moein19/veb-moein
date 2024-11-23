from django.db import models
from datetime import datetime
from posts.models import Post
from bloggers.models import Blogger

class Comments(models.Model):
    post_title = models.ForeignKey(Post, on_delete=models.DO_NOTHING,default=1)
    #user_email = models.CharField(max_length=200)
    blogger = models.ForeignKey(Blogger, on_delete=models.DO_NOTHING,default=1)
    comment_date = models.DateTimeField(default=datetime.now, blank=True)
    post_id = models.IntegerField()
    comment_text = models.TextField()

    def __str__(self) -> str:
        return self.comment_text



