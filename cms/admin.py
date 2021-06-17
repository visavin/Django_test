from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CmsSlider


# Register your models here.
class CmsAdm(admin.ModelAdmin):
    list_display = ('cms_title', 'cms_text', 'cms_css', 'get_img_for_list')
    list_display_links = ('get_img_for_list',)
    list_editable = ('cms_title', 'cms_text', 'cms_css')
    fields = ('cms_title', 'cms_text', 'cms_css', 'cms_img', 'get_img')
    readonly_fields = ('get_img',)

    def get_img_for_list(self, obj):
        if obj.cms_img:
            return mark_safe(f'<img src="{ obj.cms_img.url }" width="70px">')
        else:
            return 'нет картинки'

    def get_img(self, obj):
        if obj.cms_img:
            return mark_safe(f'<img src="{ obj.cms_img.url }" width="350px">')
        else:
            return 'нет картинки'

    get_img.short_description = 'Миниатюра'
    get_img_for_list.short_description = 'Миниатюра'


admin.site.register(CmsSlider, CmsAdm)
