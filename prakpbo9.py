import math

class VolumeCalculator:
    def volume(self, sisi=None, panjang=None, lebar=None, tinggi=None, jari_jari=None):
        if sisi is not None:
            return f"{sisi ** 3} cm^3"
        elif panjang is not None and lebar is not None and tinggi is not None:
            return f"{panjang * lebar * tinggi} cm^3"
        elif jari_jari is not None and tinggi is not None:
            return f"{math.pi * (jari_jari ** 2) * tinggi} cm^3"
        else:
            raise ValueError("Parameter tidak sesuai")

print("=============================")
nama = "Zahwa Nur Azkia Putri   |"
nim = "064002300038             |"
print("Nama:", nama)
print("NIM:", nim)
print("=============================")

calculator = VolumeCalculator()

sisi = 5
volume_kubus = calculator.volume(sisi=sisi)
print("Volume Kubus:", volume_kubus)

panjang = 4
lebar = 3
tinggi = 6
volume_balok = calculator.volume(panjang=panjang, lebar=lebar, tinggi=tinggi)
print("Volume Balok:", volume_balok)

jari_jari = 2
tinggi_tabung = 8
volume_tabung = calculator.volume(jari_jari=jari_jari, tinggi=tinggi_tabung)
print("Volume Tabung:", volume_tabung)
