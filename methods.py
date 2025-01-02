# methods.py
from db import urunler

def urunEkle(ad, fiyat):
    yeni_urun = {"id": len(urunler) + 1, "ad": ad, "fiyat": fiyat}
    urunler.append(yeni_urun)
    print(f"Ürün eklendi: {yeni_urun}")

def urunGuncelle(urun_id, yeni_ad, yeni_fiyat):
    for urun in urunler:
        if urun["id"] == urun_id:
            urun["ad"] = yeni_ad
            urun["fiyat"] = yeni_fiyat
            print(f"Ürün güncellendi: {urun}")
            return
    print(f"Ürün bulunamadı: ID {urun_id}")

def urunleriGetir():
    print("Ürün Listesi:")
    for urun in urunler:
        print(f"ID: {urun['id']}, Ad: {urun['ad']}, Fiyat: {urun['fiyat']}")