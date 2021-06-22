from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Order, StatusCrm, CommentCrm


# Register your models here.
class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ('comment_dt', 'comment_text')
    readonly_fields = ('comment_dt',)
    extra = 0


class OrderAdm(admin.ModelAdmin):
    list_display = ('order_dt', 'order_phone', 'order_name', 'order_status', 'get_comment')
    list_display_links = ('order_dt', 'order_name', 'get_comment')
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt')
    list_filter = ('order_status',)
    list_editable = ('order_status', 'order_phone')
    list_per_page = 10
    list_max_show_all = 100
    fields = ('id', 'order_dt', 'order_status', 'order_name', 'order_phone')
    readonly_fields = ('id', 'order_dt')
    # поле класса Comment
    inlines = [Comment, ]

    def get_comment(self, obj):
        comment_objects = list(CommentCrm.objects.filter(comment_binding=obj.id))
        if comment_objects:
            return mark_safe(f'<u>{comment_objects[-1].comment_text}</u>')
        else:
            return '----------'

    get_comment.short_description = 'Последний комментарий'


admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
# admin.site.register(CommentCrm)
