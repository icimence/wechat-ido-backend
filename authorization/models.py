# -*- encoding=utf8 -*-


from django.db import models

# Create your models here.


class User(models.Model):
    # openid
    open_id = models.CharField(max_length=32, unique=True)
    # 昵称
    nickname = models.CharField(max_length=256)
    # 目标专业
    major = models.TextField(default='[]')
    # 进行任务
    mission = models.TextField(default='[]')
    # 任务类别0
    type = models.TextField(default='[]')
