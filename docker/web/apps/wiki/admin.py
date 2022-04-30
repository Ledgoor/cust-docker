from django.contrib import admin
from apps.wiki.models import Page, Category

class Page_Admin (admin.ModelAdmin):
    list_filter = (['category'])
    # exclude = ['date_publish', 'date_edit']
    readonly_fields = ['date_publish', 'date_edit']

admin.site.register(Category)
# admin.site.register(Page)
admin.site.register(Page, Page_Admin)