from django.contrib import admin

from goods import models

# admin.site.register(models.Categories)
# admin.site.register(models.Products)

@admin.register(models.Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(models.Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}