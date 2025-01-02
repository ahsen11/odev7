# app.py
from methods import urunEkle, urunGuncelle, urunleriGetir

# Yeni ürün ekleme
urunEkle("iphone 15", 60000)

# Ürün güncelleme
urunGuncelle(1, "iphone 15 pro", 80000)

# Ürünleri listeleme
urunleriGetir()