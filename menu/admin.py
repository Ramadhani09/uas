from django.contrib import admin
from .models import Produk, Kategori

# Register your models here.

class Produkcafe(admin.ModelAdmin):
    list_display = ("namaproduk", "harga","jumlah",)
    
admin.site.register(Produk, Produkcafe)
admin.site.register(Kategori)