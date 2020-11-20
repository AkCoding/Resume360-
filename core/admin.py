from django.contrib import admin
from .models import Post, Profile

# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_Name', 'last_name']

admin.site.register(Profile)





