from django.contrib import admin

# Register your models here.
from .models import Category, Blog ,Comment, Post


admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Post)