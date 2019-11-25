from django.contrib import admin
from .models import Post

admin.site.register(Post) #モデルをAdminページ（管理画面）上で見えるようにする
