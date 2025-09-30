username = "mariska"
password = "052"
username=str(input("masukkan username: "))
password=str(input("masukkan password: "))
if username == "mariska" and password == "052":
    print("kalkulator multifungsi")
    konversi=str(input("masukkan konversi: "))
    if konversi == 'panjang':
        satuan=str(input("masukkan satuan: "))
        nilai=float(input("masukkan nilai: "))
        if satuan == 'kaki':
            print(nilai*0.3048,"meter")
        elif satuan == 'km':
            print(nilai*1000,"meter")
        else:
            print(nilai/100,"meter")
    if konversi == 'massa':
        satuan=str(input("masukkan satuan: "))
        nilai=float(input("masukkan nilai: "))
        if satuan == 'poun':
            print(nilai*0.45359,"kg")
        elif satuan == 'ton':
            print(nilai*1000,"kg")
        elif satuan == 'gram':
            print(nilai/1000,"kg")
        elif satuan == 'dag':
            print(nilai/100,"kg")
        else:
            print(nilai/10000,"kg")
    if konversi == 'suhu':
        satuan=str(input("masukkan satuan: "))
        nilai=float(input("masukkan nilai: "))
        if satuan == 'celcius':
            print(nilai+273.15 ,"kelvin")
        elif satuan == 'fahrenheit':
            print((nilai+459.67)*5/9,"kelvin")
        else:
            print((nilai/0.8)+273.15,"kelvin")
    if konversi == 'waktu':
        satuan=str(input("masukkan satuan: "))
        nilai=float(input("masukkan nilai: "))
        if satuan == 'menit':
            print(nilai*60, "detik")
        else:
            print(nilai*3600, "detik")
    if konversi == 'mata uang':
        satuan=str(input("masukkan satuan: "))
        nilai=float(input("masukkan nilai: "))
        if satuan == 'rupiah':
            print(nilai*0.0002531, "ringgit")
        elif satuan == 'ringgit':
            print(nilai*3.951, "rupiah")
        elif satuan == 'yen':
            print(nilai*9.429, "won")
        elif satuan == 'won':
            print(nilai*0.1061, "yen")
        elif satuan == 'dollar':
            print(nilai*0.8546, "euro")
        else:
            print(nilai*1.170, "dollar")
elif username != "mariska" and password == "052":
    print("username salah")
elif username == "mariska" and password != "052":
    print("password salah")
else:
    print("login gagal")