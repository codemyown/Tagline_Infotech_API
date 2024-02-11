from django.contrib import admin
from .models import Product, Purchase

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","price","seller"]
    
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ["product","seller","buyer","purchase_price"]

admin.site.register(Product,ProductAdmin)
admin.site.register(Purchase,PurchaseAdmin)