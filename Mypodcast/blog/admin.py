from django.contrib import admin
from .models import Article, Category, Tag, CommentArticle, Blog, CommentBlog, Season, Like


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']
    list_filter = ['category', 'created_at']
    date_hierarchy = 'created_at'
    filter_horizontal = ('tags',)


class SeasonAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Article, ArticleAdmin)
admin.site.register(CommentArticle)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Blog)
admin.site.register(CommentBlog)
admin.site.register(Like)
