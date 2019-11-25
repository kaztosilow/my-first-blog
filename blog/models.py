from django.conf import settings
from django.db import models
from django.utils import timezone

#モデル定義
class Post(models.Model): #Post　はモデルの名前、models.ModelはDjango Modelという意味でDBに保存すべきものという
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #他モデルへのリンク
    title = models.CharField(max_length=200) #文字数が制限されたテキストを定義するフィールド
    text = models.TextField() #これは制限無しの長いテキスト用です。ブログポストのコンテンツ用フィールド
    created_date = models.DateTimeField(default=timezone.now) #日時のフィールド
    publiched_date = models.DateTimeField(blank=True, null=True) #日時のフィールド

    def publish(self): #ファンクション（関数）/メソッド
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #ファンクション（関数）/メソッド
        return self.title
