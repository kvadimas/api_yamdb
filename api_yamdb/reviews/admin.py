from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('year', 'name')
    list_filter = ('year', )
    search_fields = ('name__sicontains', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('category__slug', )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ('genre__slug', )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    search_fields = ('text', )
    list_filter = ('author', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ('text', )
    list_filter = ('author', )
