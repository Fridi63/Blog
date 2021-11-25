from django.contrib import admin
from post.models import Category, Post, Comment, Like

admin.register(Category)
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
