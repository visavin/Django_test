from django.contrib import admin
from .models import PriceCard, PriceTable


# Register your models here.
class PriceTableAdm(admin.ModelAdmin):
    list_display = ('pt_title', 'pt_old_price', 'pt_new_price')
    list_display_links = None
    list_editable = ('pt_title', 'pt_old_price', 'pt_new_price')


admin.site.register(PriceCard)
admin.site.register(PriceTable, PriceTableAdm)
