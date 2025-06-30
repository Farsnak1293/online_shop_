from django.contrib import admin
from .models import Product,Comment


class CommentsInline(admin.TabularInline):
    model = Comment
    fields = ('author', 'body', 'recommend', 'active',)
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'active',  )

    inlines = [
        CommentsInline,

    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'recommend','product' ,'active', )


