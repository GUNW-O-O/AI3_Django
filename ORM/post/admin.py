from django.contrib import admin

# Register your models here.
# admin.py
from .models import Post
admin.site.register(Post)
