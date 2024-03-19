from django.contrib import admin
from template_app.models import Category, Page


# /|\ Fix this

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)

## This adds the given aspects from models.py to the admin page
