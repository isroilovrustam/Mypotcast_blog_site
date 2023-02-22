from django.contrib import admin
from .models import Contact, Subscribe


# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ['Name', 'created_at', 'is_published', 'id']
    list_filter = ['is_published']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Subscribe)
