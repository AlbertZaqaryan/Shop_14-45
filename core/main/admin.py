from django.contrib import admin
from .models import (HomeLogo, HomeCarusel, 
                    Category, SubCategory, Product,
                    Filter, Filter_product, Card)
# Register your models here.

admin.site.register(HomeLogo)
admin.site.register(HomeCarusel)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Filter)
admin.site.register(Filter_product)
admin.site.register(Card)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name', 'price']
