while True:
    user = input("masukkan username: ")
    while user == "":
        user = input("masukkan user dong: ")
    pw = input("Masukkan password: ")
    while pw == "":
        pw = input("Masukkan pw dong: ")
    if user != "mariska" and pw == "052":
        print("username salah")
    elif user == "mariska" and pw != "052":
        print("password salah")
    elif user == "mariska" and pw == "052":
        print("login berhasil")
        break
    else:
        print("username dan password salah, coba lagi")

print("\n -- PROGRAM MENGELOLA STOK DARAH --")
Total_A_plus = 0
total_A_min = 0
total_B_plus = 0
total_B_min = 0
total_O_plus = 0
total_O_min = 0
total_AB_plus = 0
total_AB_min = 0
total_golongandarah = 0

ulangi = "ya"
while ulangi == "ya":
    print("\nMasukkan golongan darah ")
    tipe = input("tipe golongan darah (A/B/O/AB): ")
    while tipe == "":
        tipe = input("golongan darahnya apa nih: ")
    if tipe == "A":
        rhesus = input("masukkan rhesus (A+/A-): ")
        while rhesus == "":
            rhesus = input("kamu belum masukkan rhesus: ")
        if rhesus == "A+":
            print("tipe: A+")
        else:
            print("tipe: A-")

    elif tipe == "B":
        rhesus = input("masukkan rhesus (B+/B-): ")
        while rhesus == "":
            rhesus = input("kamu belum masukkan rhesus: ")
        if rhesus == "B+":
            print("tipe: B+")
        else:
            print("tipe: B-")

    elif tipe == "O":
        rhesus = input("masukkan rhesus (O+/O-): ")
        while rhesus == "":
            rhesus = input("kamu belum masukkan rhesus: ")
        if rhesus == "O+":
            print("tipe: O+")
        else:
            print("tipe: O-")

    elif tipe == "AB":
        rhesus = input("masukkan rhesus (AB+/AB-): ")
        while rhesus == "":
            rhesus = input("kamu belum masukkan rhesus: ")
        if rhesus == "AB+":
            print("tipe: AB+")
        else:
            print("tipe: AB-")

    else:
        print("tipe tidak valid!\n")
        continue 

    jumlah = input("Masukkan jumlah kantong darah: ")
    while jumlah == "":
        jumlah = input("jumlah gak boleh kosong,masukkan jumlah: ")
    jumlah = int(jumlah)
    print("Jumlah kantong:", jumlah, "\n")

    if rhesus == "A+":
        Total_A_plus += jumlah
    elif rhesus == "A-":
        total_A_min += jumlah
    elif rhesus == "B+":
        total_B_plus += jumlah
    elif rhesus == "B-":
        total_B_min += jumlah
    elif rhesus == "O+":
        total_O_plus += jumlah
    elif rhesus == "O-":
        total_O_min += jumlah
    elif rhesus == "AB+":
        total_AB_plus += jumlah
    elif rhesus == "AB-":
        total_AB_min += jumlah
    ulangi = input("apakah masih mau input lagi (ya/tidak): ")
    while ulangi == "":
        ulangi = input("jawab dong (ya/tidak): ")

print("\n-- JUMLAH AKHIR GOLONGAN DARAH --")
print("Total golongan darah A+ :", Total_A_plus * 500, "ml")
print("Total golongan darah A- :", total_A_min * 500, "ml")
print("Total golongan darah B+ :", total_B_plus * 500, "ml")
print("Total golongan darah B- :", total_B_min * 500, "ml")
print("Total golongan darah O+ :", total_O_plus * 500, "ml")
print("Total golongan darah O- :", total_O_min * 500, "ml")
print("Total golongan darah AB+ :", total_AB_plus * 500, "ml")
print("Total golongan darah AB- :", total_AB_min * 500, "ml")