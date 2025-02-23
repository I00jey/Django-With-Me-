from django.contrib import admin
from .models import Post
# Register your models here.

# 관리자가 게시글에 접근할 권한 부여
admin.site.register(Post)