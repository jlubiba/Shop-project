from django.contrib import admin
from .models import Category, ProductList, Cart, Order, OrderProduct

# Register your models here.
# This makes it such that when the 'name' field is being filled, the 'slug' field is automatically field at the same time when done in the admin panel.
class AutoSlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Category, AutoSlugAdmin)
admin.site.register(Cart)
admin.site.register(ProductList)
admin.site.register(Order)
admin.site.register(OrderProduct)
