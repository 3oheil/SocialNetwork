from django.contrib import admin

from .models import Post, PostFile


class PostFileInlinesAdmin(admin.StackedInline):
    model = PostFile
    fields = ('file',)
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'create_date')
    inlines = (PostFileInlinesAdmin,)
