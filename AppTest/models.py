from django.db import models

# Create your models here.

GAMETYPE_CHOICE = (
    ("主包", "主包"),
    ("独立包", "独立包"),
    ("钱包", "钱包")
)

TORT_CHOICE = (
    ("普通侵权", "普通侵权"),
    ("中度侵权", "中度侵权"),
    ("重度侵权", "重度侵权"),
    ("非侵权", "非侵权")
)

REGION_CHOICE = (
    ("东南亚", "东南亚"),
    ("美国", "美国"),
    ("中东", "中东"),
    ("泰国", "泰国"),
    ("越南", "越南"),
)

LANGUAGE_CHOICE = (
    ("中英文", "中英文"),
    ("简中", "简中"),
    ("英文", "英文"),
    ("泰语", "泰语"),
    ("越南语", "越南语"),
    ("俄语", "俄语"),
    ("德语", "德语"),
    ("印尼语", "印尼语"),
    ("阿拉伯语", "阿拉伯语"),
)

ENGINE_CHOICE = (
    ("Unity3D", "Unity3D"),
    ("Cocos2D", "Cocos2D"),
    ("Flash Air", "Flash Air")
)

STATUS_CHOICE = (
    ("未上线","未上线"),
    ("已上线", "已上线"),
    ("已下架", "已下架"),
)

ACCOUNTTYPE_CHOICE = (
    ("游戏包账号", "游戏包账号"),
    ("钱包账号", "钱包账号"),
    ("测试账号", "测试账号")
)


class GameInfo(models.Model):
    gameName = models.CharField(max_length=100, verbose_name="游戏名称")
    gameCode = models.CharField(max_length=20, verbose_name="游戏编码")
    gameType = models.CharField(max_length=20, verbose_name="游戏包类型", choices=GAMETYPE_CHOICE)
    parentGame = models.CharField(max_length=20, verbose_name="主包gamecode")
    tort = models.CharField(max_length=20, verbose_name="侵权类型", choices=TORT_CHOICE)
    packageName = models.CharField(max_length=50, verbose_name="包名")
    versionCode = models.CharField(max_length=20, verbose_name="版本号")
    versionName = models.CharField(max_length=30, verbose_name="版本名称")
    language = models.CharField(max_length=20, verbose_name="游戏语言", choices=LANGUAGE_CHOICE)
    region = models.CharField(max_length=30, verbose_name="地区", choices=REGION_CHOICE)
    engine = models.CharField(max_length=30, verbose_name="游戏引擎", choices=ENGINE_CHOICE)
    status = models.CharField(max_length=20, verbose_name="游戏状态", default="未上线", choices=STATUS_CHOICE)

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
    accountType = models.CharField(max_length=50, verbose_name="账号类型", default="游戏包账号", choices=ACCOUNTTYPE_CHOICE)

    def __str__(self):
        return self.gameName + "(" + self.gameCode + ")"

    class Meta:
        verbose_name = "开发者账号管理"
