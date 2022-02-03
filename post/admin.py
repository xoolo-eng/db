from django.contrib import admin
from post.models import Post, Tag


admin.site.register(Tag)
admin.site.register(Post)