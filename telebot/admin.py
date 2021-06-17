from django.contrib import admin
from .models import TeleSettings


# Register your models here.
class TgAdm(admin.ModelAdmin):
    list_display = ('tg_token', 'tg_chat', 'tg_text')
    list_display_links = None
    list_editable = ('tg_token', 'tg_chat', 'tg_text')


admin.site.register(TeleSettings, TgAdm)
