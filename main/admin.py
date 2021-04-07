from django.contrib import admin

# Register your models here.
from .models import *

class ImageInLineAdmin(admin.TabularInline):
    model = Image
    fields = ('image',)
    max_num = 5

@admin.register(Post)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [ImageInLineAdmin,]

admin.site.register(Category)


#Comment
