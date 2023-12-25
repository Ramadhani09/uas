from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Kategori, Produk
from .form import FormProduk

# Create your views here.
def home(request):
    home = loader.get_template('home.html')
    return HttpResponse(home.render())

def produk(request):
    submitted = False
    if request.method == "POST":
        form = FormProduk(request.POST)
        if form.is_valid():
            simpandata = Produk.objects.create(
                Kategori = form.cleaned_data.get("kategori"),
                namaproduk = form.cleaned_data.get("namaproduk"),
                harga = form.cleaned_data.get("harga"),
                jumlah = form.cleaned_data.get("jumlah"),
            )
        simpandata.save()
        return HttpResponseRedirect("/produk?submitted=True")
    else:
        form = FormProduk
        if "submitted" in request.GET:
            submitted = True

    data = Kategori.objects.all()
    data_produk = Produk.objects.all()
    context = {
        "judul":"Selamat Datang di Website",
        "subjudul":"My Website No 2",
        "kategori": data,
        "data_produk": data_produk,
        "form" : FormProduk,
        "submitted" : submitted,
    }
    produk = loader.get_template('produk.html')
    return HttpResponse(produk.render(context,request))

def detail_produk(request, id):
  data_produk = Produk.objects.get(id=id)
  context = {
    "produk": data_produk,
  }
  template = loader.get_template('detailproduk.html')
  return HttpResponse(template.render(context, request))
 

def kategori(request):
    data_produk = Produk.objects.all()
    kategori = loader.get_template('kategori.html')
    return HttpResponse(kategori.render())

# def base(request):
#     base = loader.get_template('base.html')
#     return HttpResponse(base.render())e.
