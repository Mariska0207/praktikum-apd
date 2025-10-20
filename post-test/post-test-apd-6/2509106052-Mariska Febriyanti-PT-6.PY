from tabulate import tabulate
import os
login_admin = False
login_user = False
anggota = {
    "user": "admin",
    "pw": "admin123"
}
barang = {
    1 : {"nama barang" : "tenda 2 orang", "stok" : 10, "harga" : 50000, "status" : "tersedia"},
    2 : {"nama barang" : "kursi lipat", "stok" : 15, "harga" : 15000, "status" : "tersedia"},
    3 : {"nama barang" : "meja lipat", "stok" : 8, "harga" : 10000, "status" : "tersedia"}
}

baris1 = "^"*50
baris2 = "="*50
baris3 = "~"*50
baris4 = "_"*50

while True:
    os.system("cls || clear")
    print("TOKO PENYEWAAN ALAT CAMPING \n1. admin \n2. pengguna biasa \n3. Registrasi  \n4. Keluar")
    menu = input("pilih menu (1/2/3/4): ")
    os.system("cls || clear")

    if menu == "1":
        print(baris2)
        print("LOGIN SEBAGAI ADMIN".center(50))
        print(baris2)
        user = input("username: ")
        pw = input("password: ")
        if user == "admin" and pw == "admin123":
            print(baris1)
            print("Anda berhasil masuk sebagai admin".center(50))
            print(baris1)
            input("enter untuk lanjut....")
            login_admin = True
            login_user = False
            break
        else:
            print("!!! login sebagai admin gagal, silahkan coba lagi !!!".center(50))
            input("enter untuk kembali ke menu....")

    elif menu == "2":
        print(baris2)
        print("LOGIN SEBAGAI PENGGUNA BIASA".center(50))
        print(baris2)
        user = input("username: ")
        pw = input("password: ")
        if anggota["user"] == user and anggota["pw"] == pw:
            print(baris1)
            print("Anda berhasil masuk".center(50))
            print(baris1)
            input("enter untuk lanjut....")
            login_admin = False
            login_user = True
            break
        else:
            print("!!!!! login gagal, silahkan coba lagi atau silahkan registrasi !!!!!".center(50))
            input("enter untuk kembali ke menu....")

    elif menu == "3":
        print(baris2)
        print("SILAHKAN REGISTRASI".center(50))
        print(baris2)
        userbaru = input("Username: ")
        pwbaru = input("Password: ")
        anggota["user"] = userbaru
        anggota["pw"] = pwbaru
        print(baris3)
        print(f"Berhasil, username {userbaru} telah terdaftar".center(50))
        print(baris3)
        input("enter untuk kembali ke menu....")

    elif menu == "4":
        input("enter untuk keluar...")
        login_admin = False
        login_user = False
        break
    else:
        print("!!!!! pilihan tidak valid, coba lagi !!!!!".center(50))
        input("enter untuk kembali ke menu....")

while True:
    if login_user:
        while login_user:
            os.system("cls || clear")
            print("SILAHKAN PILIH OPSI")
            print("1. Lihat barang \n2. sewa barang \n3. keluar")
            menu_user = input("masukkan pilihan (1/2/3): ")
            os.system("cls || clear")
            if menu_user == "1":
                print(baris2)
                print("DAFTAR BARANG".center(50))
                print(baris2)
                if len(barang) == 0:
                    print(baris1)
                    print("belum ada barang tersedia".center(50))
                    print(baris1)
                    input("enter untuk kembali ke menu....")
                else:
                    for i, j in barang.items():
                        if j["stok"] == 0:
                            j["status"] = "habis"
                        else:
                            j["status"] = "tersedia"
                    head = ["No","Nama barang", "stok", "harga", "status"]
                    listbarang = [
                        [ i, j["nama barang"], j["stok"], j["harga"], j["status"]]
                        for i, j in barang.items()
                    ]
                    print(tabulate(listbarang,headers=head, tablefmt="fancy_grid"))
                    input("enter untuk kembali ke menu....")
            elif menu_user == "2":
                print(baris2)
                print("PENYEWAAN BARANG".center(50))
                print(baris2)
                if len(barang) == 0:
                    print(baris1)
                    print("belum ada barang tersedia".center(50))
                    print(baris1)
                    input("enter untuk kembali ke menu....")
                else:
                    head = ["No","Nama barang", "stok", "harga", "status"]
                    listbarang = [
                        [ i, j["nama barang"], j["stok"], j["harga"], j["status"]]
                        for i, j in barang.items()
                    ]
                    print(tabulate(listbarang,headers=head, tablefmt="fancy_grid"))
                    pilih = int(input("masukkan nomor barang yang ingin di sewa: "))
                    print(baris4)
                    jumlah = int(input("jumlah barang yang di sewa: "))
                    print(baris4)
                    if pilih in barang:
                        stokawal = barang[pilih]["stok"]
                        if jumlah > stokawal:
                            print("!!!!! stok tidak mencukupi !!!!!".center(50))
                            input("enter untuk kembali ke menu....")
                        else:
                            stokbaru = stokawal - jumlah
                            barang[pilih]["stok"] = stokbaru
                            print(baris4)
                            input("enter untuk kembali ke menu....")

            elif menu_user == "3":
                input("enter untuk keluar...")
                login_user = False
                break
            else:
                print("!!!!! pilihan tidak valid,coba lagi !!!!!".center(50))
                input("enter untuk kembali ke menu....")

    elif login_admin:
        while login_admin:
            os.system("cls || clear")
            print("SILAHKAN PILIH OPSI")
            print("1. Tambah Barang \n2. Lihat barang \n3. Perbarui barang \n4. Hapus Barang \n5. Keluar")
            menu_admin = input("masukkan pilihan (1/2/3/4/5): ")
            os.system("cls || clear")
            if menu_admin == "1":
                print(baris2)
                print("MENAMBAHKAN BARANG".center(50))
                print(baris2)
                narang =  input("Nama barang: ")
                sama = False
                for i in barang:
                    if barang[i]["nama barang"] == narang:
                        sama = True
                        break
                if sama:
                    print("barang sudah ada, masukkan barang lain")
                    input("enter untuk kembali ke menu....")
                else:
                    newstok = input("Stok: ")
                    newharga = input("Harga: ")
                    newstatus = input("Status: ")
                for i in barang:    
                    tambah = i + 1
                barang[tambah]={
                    "nama barang" : narang, "stok" : newstok, "harga" : newharga, "status" : newstatus
                }
                print(baris3)
                print(f"{narang} berhasil ditambahkan".center(50))
                print(baris3)
                input("enter untuk kembali ke menu....")

            elif menu_admin == "2":
                print(baris2)
                print("DAFTAR BARANG".center(50))
                print(baris2)
                if len(barang) == 0:
                    print(baris1)
                    print("belum ada barang tersedia".center(50))
                    print(baris1)
                    input("enter untuk kembali ke menu....")
                else:
                    head = ["No","Nama barang", "stok", "harga", "status"]
                    key = list(barang.keys())
                    listbarang = [
                        [i + 1, barang[key[i]]["nama barang"], barang[key[i]]["stok"], barang[key[i]]["harga"], barang[key[i]]["status"]]
                        for i in range(len(key))
                    ]
                    print(tabulate(listbarang,headers=head, tablefmt="fancy_grid"))
                    input("enter untuk kembali ke menu....")

            elif menu_admin == "3":
                print(baris2)
                print("PERBARUI BARANG".center(50))
                print(baris2)
                if len(barang) == 0:
                    print(baris1)
                    print("belum ada barang tersedia".center(50))
                    print(baris1)
                    input("enter untuk kembali ke menu....")
                else:
                    head = ["No","Nama barang", "stok", "harga", "status"]
                    key = list(barang.keys())
                    listbarang = [
                        [i + 1, barang[key[i]]["nama barang"], barang[key[i]]["stok"], barang[key[i]]["harga"], barang[key[i]]["status"]]
                        for i in range(len(key))
                    ]
                    print(tabulate(listbarang,headers=head, tablefmt="fancy_grid"))
                    pilih = int(input("masukkan nomor yang mau diperbarui: "))
                    key = list(barang.keys())[pilih-1]
                    narang = input("Nama barang: ")
                    while narang == "":
                        narang = input("inputan tidak boleh kosong, masukkan nama barang: ")
                    newstok = input("Stok: ")
                    while newstok == "":
                        newstok = input("inputan tidak boleh kosong, masukkan stok: ")
                    newharga = input("Harga: ")
                    while newharga == "":
                        newharga = input("inputan tidak boleh kosong, masukkan harga: ")
                    newstatus = input("Status: ")
                    while newstatus == "":
                        newstatus = input("inputan tidak boleh kosong, masukkan status: ")
                    barang[key]={
                        "nama barang" : narang, "stok" : newstok, "harga" : newharga, "status" : newstatus
                    }
                    print(baris3)
                    print("barang berhasil di perbarui".center(50))
                    print(baris3)
                    input("enter untuk kembali ke menu....")

            elif menu_admin == "4":
                print(baris2)
                print("MENGHAPUS BARANG".center(50))
                print(baris2)
                if len(barang) == 0:
                    print(baris1)
                    print("belum ada barang tersedia".center(50))
                    print(baris1)
                    input("enter untuk kembali ke menu....")
                else:
                    head = ["No","Nama barang", "stok", "harga", "status"]
                    key = list(barang.keys())
                    listbarang = [
                        [i + 1, barang[key[i]]["nama barang"], barang[key[i]]["stok"], barang[key[i]]["harga"], barang[key[i]]["status"]]
                        for i in range(len(key))
                    ]
                    print(tabulate(listbarang,headers=head, tablefmt="fancy_grid"))
                    pilih = int(input("masukkan nomor yang ingin dihapus: "))
                    key = list(barang.keys())[pilih-1]
                    del barang[key]
                    print(baris3)
                    print("barang berhasil di hapus".center(50))
                    print(baris3)
                    input("enter untuk kembali ke menu....")

            elif menu_admin == "5":
                input("enter untuk keluar...")
                login_admin = False
                break
            else:
                print("!!!!! pilihan tidak valid,coba lagi !!!!!".center(50))
                input("enter untuk kembali ke menu....")

    else:           
        os.system('cls || clear')
        print(baris3)
        print("ANDA TELAH KELUAR".center(50))
        print("TERIMA KASIH SUDAH MENGGUNAKAN PROGRAM INI".center(50))
        print(baris3)
        break