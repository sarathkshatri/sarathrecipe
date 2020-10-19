from django.contrib import admin
from .models import Recipe, Category, Favorite, Substance, Ingredients, Comment


class CategoryList(admin.ModelAdmin):
    list_display = ('')


class SubstanceList(admin.ModelAdmin):
    list_display = ('pk', 'substance_name')

# Register your models here.
admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Favorite)
admin.site.register(Substance, SubstanceList)
admin.site.register(Ingredients)
admin.site.register(Comment)
