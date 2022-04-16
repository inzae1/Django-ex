from django.db import models


# 제일 처음 모델을 생성해야함
# 데이터와 관련된 코드
class Article(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    url = models.URLField()
    email = models.EmailField()
    cdate = models.DateTimeField(auto_now_add=True)
