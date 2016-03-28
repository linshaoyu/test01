from django.contrib import admin
from .models import *

# Register your models here.


class GameInfoAdmin(admin.ModelAdmin):
    list_display = ("gameName", "gameCode", "gameType",)
    search_fields = ("gameCode",)


class AccountInfoAdmin(admin.ModelAdmin):
    list_display = ("gameName", "gameCode", "accountType", )
    search_fields = ("gameCode",)


admin.site.register(GameInfo, GameInfoAdmin)
admin.site.register(AccountInfo, AccountInfoAdmin)

