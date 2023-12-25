from django import forms 
from .models import Kategori

class FormProduk(forms.Form):
    kategori = forms.ModelChoiceField(queryset=Kategori.objects.all())
    namaproduk= forms.CharField()
    harga = forms.CharField( max_length=20)
    jumlah = forms.IntegerField()