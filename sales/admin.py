from django.contrib import admin
from .models import ArticleCategory, Article, Sale


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('display_name',)
    list_filter = ('display_name',)
    search_fields = ('display_name',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('code', 'category', 'name', 'manufacturing_cost')
    list_filter = ('category',)
    search_fields = ('code', 'name')


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'author', 'article', 'quantity', 'unit_selling_price')
    list_filter = ('date', 'author',)
    search_fields = ('id', 'article__code', 'article__name')
    list_per_page = 25

    def has_change_permission(self, request, obj=None):
        if obj is not None and request.user == obj.author:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj is not None and request.user == obj.author:
            return True
        return False
