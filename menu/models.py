from django.db import models

# Create your models here.
class Kategori(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nama}"
    
class Produk(models.Model):
    Kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    namaproduk = models.CharField(max_length=100)
    gmbr_produk = models.ImageField(null=True, blank=True, upload_to="images/")
    harga = models.CharField(max_length=20)
    jumlah = models.IntegerField()

    def __str__(self):
        return f"{self.namaproduk} {self.harga} {self.jumlah}"