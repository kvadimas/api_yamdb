from django.contrib import admin

from users.models import User
from .models import Category, Comment, Genre, Review, Title


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'username', 'email', 'first_name', 'last_name', 'bio', 'role')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('role',)
    list_editable = ('role',)
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name', )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ('name', )


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'year')
    list_filter = ('year', )
    search_fields = ('name', 'year', 'description', 'genre', 'category')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    search_fields = ('text', )
    list_filter = ('author', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ('text', )
    list_filter = ('author', )
