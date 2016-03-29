from django.contrib import admin
from .models import *


# Register your models here.


class GameInfoAdmin(admin.ModelAdmin):
    list_display = (
        "gameName", "gameCode", "gameType", "parentGame", "tort", "packageName", "language", "region", "engine",
        "status",)
    search_fields = ("gameCode",)


class AccountInfoAdmin(admin.ModelAdmin):
    list_display = (
    "gameName", "gameCode", "account", "password", "accUser", "devIp", "devAccount", "devPassword", "accountType",)
    search_fields = ("gameCode",)


admin.site.register(GameInfo, GameInfoAdmin)
admin.site.register(AccountInfo, AccountInfoAdmin)
