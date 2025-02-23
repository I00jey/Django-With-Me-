from django.db import models

# Create your models here.

# 모델 => 붕어빵을 만드는 틀
# 게시글 Post
# 제목 postname
# 내용 contents
class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()