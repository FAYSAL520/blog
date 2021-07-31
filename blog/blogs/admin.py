from django.contrib import admin
from.models import *


# Register your models here.

@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_category', 'pub_date')


@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ('email', 'phone', 'timeStamp')



admin.site.register(BlogsCategory)

admin.site.register(BlogSubCategory)