from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Money(models.Model):
    use_date = models.DateTimeField('日付')
    detail = models.CharField(max_length=200)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.detail + ' ￥' + str(self.cost)
