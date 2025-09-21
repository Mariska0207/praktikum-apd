suhu = [27, 33, 46, 55, 67, 92]
print(f"suhu {suhu}")

#konversi suhu
suhu1 = (9/5) * suhu[0] + 32
print(f"Fahrenheit {suhu1}")
suhu2 = (9/5) * suhu[1] + 32
print(f"Fahrenheit {suhu2}")
suhu3 = suhu[2] + 273.15
print(f"Kelvin {suhu3}")
suhu4 = suhu[3] + 273.15
print(f"Kelvin {suhu4}")
suhu5 = (4/5) * suhu[4]
print(f"Reamur {suhu5}")
suhu6 = (4/5) * suhu[5]
print(f"Reamur {suhu6}")

#jumlahkan
jumlah = suhu1 + suhu2 + suhu3 + suhu4 + suhu5 + suhu6
print(f"jumlah {jumlah}")

#rata-rata
rata_rata = jumlah/6
print(f"rata-rata {rata_rata}")

NIM = 52
bool = NIM < rata_rata
print(f"boolean {bool}")