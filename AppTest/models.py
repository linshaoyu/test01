from django.db import models


# Create your models here.

class GameInfo(models.Model):
    gameName = models.CharField(max_length=100, verbose_name="游戏名称")
    gameCode = models.CharField(max_length=20, verbose_name="游戏编码")
    gameType = models.CharField(max_length=20, verbose_name="游戏包类型")
    parentGame = models.CharField(max_length=20, verbose_name="主包gamecode")
    tort = models.CharField(max_length=20, verbose_name="侵权类型")
    packageName = models.CharField(max_length=50, verbose_name="包名")
    versionCode = models.CharField(max_length=20, verbose_name="版本号")
    versionName = models.CharField(max_length=30, verbose_name="版本名称")
    language = models.CharField(max_length=20, verbose_name="游戏语言")
    region = models.CharField(max_length=30, verbose_name="地区")
    engine = models.CharField(max_length=30, verbose_name="游戏引擎")
    status = models.CharField(max_length=20, verbose_name="游戏状态", default="已上线")

    def __str__(self):
        return self.gameName + "(" + self.gameCode + ")"

    class Meta:
        verbose_name = "游戏信息管理"


class AccountInfo(models.Model):
    gameName = models.CharField(max_length=100, verbose_name="游戏名称")
    gameCode = models.CharField(max_length=20, verbose_name="游戏编码")
    account = models.CharField(max_length=50, verbose_name="开发者账号")
    password = models.CharField(max_length=50, verbose_name="账号密码")
    accUser = models.CharField(max_length=50, verbose_name="账号名称")
    devIp = models.CharField(max_length=50, verbose_name="远程设备IP")
    devAccount = models.CharField(max_length=50, verbose_name="远程账号")
    devPassword = models.CharField(max_length=50, verbose_name="远程密码")
    accountType = models.CharField(max_length=50, verbose_name="账号类型", default="-")

    def __str__(self):
        return self.gameName + "(" + self.gameCode + ")"

    class Meta:
        verbose_name = "开发者账号管理"
