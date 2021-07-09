from django.contrib import admin
from products.models import *


class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Products
    search_fields = ['title', 'descriptions']
    list_display = 'id title category price'.split()
    list_filter = 'category'.split()


admin.site.register(Category)
admin.site.register(Products, ProductAdmin)
admin.site.register(Review)
admin.site.register(Tag)
