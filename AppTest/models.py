from django.db import models


# Create your models here.

class GameInfo(models.Model):
    gameName = models.CharField(max_length=100)
    gameCode = models.CharField(max_length=20)
    gameType = models.CharField(max_length=20)
    parentGame = models.CharField(max_length=20)
    tort = models.CharField(max_length=20)
    versionCode = models.IntegerField
    versionName = models.CharField(max_length=30)
    engine = models.CharField(max_length=30)


class AccountInfo(models.Model):
    gameName = models.CharField(max_length=100)
    gameCode = models.CharField(max_length=20)
    account = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    accUser = models.CharField(max_length=50)
    packageName = models.CharField(max_length=50)
    devIp = models.CharField(max_length=50)
    devAccount = models.CharField(max_length=50)
    devPassword = models.CharField(max_length=50)
    accountType = models.CharField(max_length=50)