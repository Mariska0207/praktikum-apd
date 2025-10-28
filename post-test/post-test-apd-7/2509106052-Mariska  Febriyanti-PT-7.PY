from tabulate import tabulate
import os
kesempatanlogin = 3
anggota = {
    "user": "mar",
    "pw": "052"
}
barang = {
    1 : {"nama barang" : "tenda 2 orang", "stok" : 10, "harga" : 50000, "status" : "tersedia"},
    2 : {"nama barang" : "kursi lipat", "stok" : 15, "harga" : 15000, "status" : "tersedia"},
    3 : {"nama barang" : "meja lipat", "stok" : 8, "harga" : 10000, "status" : "tersedia"}
}

garis2 = "="*50
def judul(teks):
    print(garis2)
    print(teks.center(50))
    print(garis2)

garis1 = "^"*50
def info(teks):
    print(garis1)
    print(teks.center(50))
    print(garis1)

def jumlahbarang(barang):
    if len(barang) == 0:
        print("BARANG KOSONG".center(50))

def jumlahtersedia():
    tersedia = 0
    for i in barang:
        if barang[i]["status"] == "tersedia":
            tersedia += 1
    return tersedia

def daftarbarang(barang):
    jumlahbarang(barang)
    for i, j in barang.items():
        if j["stok"] == 0:
            j["status"] = "habis"
        else:
            j["status"] = "tersedia"
    head = ["No","Nama barang", "stok", "harga", "status"]
    key = list(barang.keys())
    listbarang = [
        [i + 1, barang[key[i]]["nama barang"], barang[key[i]]["stok"], barang[key[i]]["harga"], barang[key[i]]["status"]]
        for i in range(len(key))
    ]
    print(tabulate(listbarang,headers=head, tablefmt="fancy_grid"))
    print(f"jumlah barang tersedia: {jumlahtersedia()}\n")
    return listbarang

def totalbayar(harga,jumlah):
    total = harga * jumlah
    print(f"total bayar: Rp {total}")
    return total

def sewabarang():
    daftarbarang(barang)
    try:
        pilih = int(input("masukkan nomor barang yang ingin di sewa: "))
        if pilih in barang:
            stokawal = barang[pilih]["stok"]
            harga = barang[pilih]["harga"]
            jumlah = int(input("jumlah barang yang di sewa: "))
            if jumlah > stokawal:
                print("!!!!! stok tidak mencukupi !!!!!".center(50))
            else:
                stokbaru = stokawal - jumlah
                barang[pilih]["stok"] = stokbaru
                totalbayar(harga,jumlah)
        else:
            print("nomor tidak valid, coba lagi")
    except ValueError:
        print("!!!!! Input harus berupa angka. Silakan coba lagi. !!!!!".center(50))

def tambahbarang():
    try:
        narang =  input("Nama barang: ")
        if narang == "":
            raise ValueError("input kosong")
        for i in barang:
            if barang[i]["nama barang"] == narang:
                print("barang sudah ada, masukkan barang lain")
                return
        try:
            newstok = int(input("Stok: "))
            newharga = int(input("Harga: "))
        except ValueError:
            print("inputan hanya angka")
            return
        newstatus = input("Status(tersedia/habis): ")
        if newstatus not in ["tersedia", "habis"]:
            raise ValueError("inputan hanya boleh tersedia/habis ")
        for i in barang:    
            tambah = i + 1
        barang[tambah]={
            "nama barang" : narang, "stok" : newstok, "harga" : newharga, "status" : newstatus
        }
        info(f"{narang} berhasil ditambahkan")
    except ValueError as e:
        print(e)

def perbaruibarang():
    daftarbarang(barang)
    try:
        pilih = int(input("masukkan nomor yang mau diperbarui: "))
        for pilih in barang:
            i = pilih
            break
        else:
            print("nomor tidak valid, coba lagi")
    except ValueError:
        print("!!!!! Input harus berupa angka. Silakan coba lagi. !!!!!".center(50))
        return
    try:
        narang =  input("Nama barang: ")
        if narang == "":
            raise ValueError("input kosong")
        for i in barang:
            if barang[i]["nama barang"] == narang:
                print("barang sudah ada, masukkan barang lain")
                input("enter untuk kembali ke menu....")
                return
        try:
            newstok = int(input("Stok: "))
            newharga = int(input("Harga: "))
        except ValueError:
            print("inputan hanya angka")
            return
        newstatus = input("Status(tersedia/habis): ")
        if newstatus not in ["tersedia", "habis"]:
            raise ValueError("inputan hanya boleh tersedia/habis ")
        barang[i]={
            "nama barang" : narang, "stok" : newstok, "harga" : newharga, "status" : newstatus
        }
        info("barang berhasil di perbarui")
    except ValueError as e:
        print(e)

def hapusbarang():
    daftarbarang(barang)
    try:
        pilih = int(input("masukkan nomor yang ingin dihapus: "))
        key = list(barang.keys())[pilih-1]
        del barang[key]
        info("barang berhasil di hapus")
    except (ValueError,IndexError):
        print("!!!!! Kesalahan inputan. Silakan coba lagi. !!!!!".center(50))

def loginuser():
    while True:
        os.system("cls || clear")
        print("SILAHKAN PILIH OPSI \n1. Lihat barang \n2. sewa barang \n3. keluar")
        menu_user = input("masukkan pilihan (1/2/3): ")
        os.system("cls || clear")

        if menu_user == "1":
            judul("DAFTAR BARANG")
            daftarbarang(barang)
            input("enter untuk kembali ke menu....")
        elif menu_user == "2":
            judul("PENYEWAAN BARANG")
            sewabarang()
            input("enter untuk kembali ke menu....")

        elif menu_user == "3":
            input("enter untuk keluar...")
            break
        else:
            print("!!!!! pilihan tidak valid,coba lagi !!!!!".center(50))
            input("enter untuk kembali ke menu....")

def loginadmin():
    while True:
        os.system("cls || clear")
        print("SILAHKAN PILIH OPSI \n1. Tambah Barang \n2. Lihat barang \n3. Perbarui barang \n4. Hapus Barang \n5. Keluar")
        menu_admin = input("masukkan pilihan (1/2/3/4/5): ")
        os.system("cls || clear")

        if menu_admin == "1":
            judul("MENAMBAHKAN BARANG")
            tambahbarang()
            input("enter untuk kembali ke menu....")

        elif menu_admin == "2":
            judul("DAFTAR BARANG")
            daftarbarang(barang)
            input("enter untuk kembali ke menu....")

        elif menu_admin == "3":
            judul("PERBARUI BARANG")
            perbaruibarang()
            input("enter untuk kembali ke menu....")

        elif menu_admin == "4":
            judul("MENGHAPUS BARANG")
            hapusbarang()
            input("enter untuk kembali ke menu....")

        elif menu_admin == "5":
            input("enter untuk keluar...")
            break
        else:
            print("!!!!! pilihan tidak valid,coba lagi !!!!!".center(50))
            input("enter untuk kembali ke menu....")      

def login():
    global kesempatanlogin
    judul("LOGIN")
    try:
        user = input("username: ")
        pw = input("password: ")
        if user == "" or pw == "":
            raise ValueError("input tidak boleh kosong")
        if user == "admin" and pw == "admin123":
            info("Anda berhasil masuk sebagai admin")
            input("enter untuk lanjut....")
            loginadmin()
        elif anggota["user"] == user and anggota["pw"] == pw:
            info("Anda berhasil masuk")
            input("enter untuk lanjut....")
            loginuser()
        else:
            kesempatanlogin -= 1
            if kesempatanlogin > 0:
                print(f"Login anda Gagal, kesempatan login tersisa {kesempatanlogin}")
                input("enter untuk kembali ke menu....")
                return login()
            else:
                print("kesempatan anda habis")
                input("enter untuk keluar")
                exit()
    except ValueError as e:
        print(e)

def registrasi():
    judul("REGISTRASI")
    try:
        userbaru = input("Username: ")
        pwbaru = input("Password: ")
        if userbaru == "" or pwbaru == "":
            raise ValueError("input tidak boleh kosong")
        anggota["user"] = userbaru
        anggota["pw"] = pwbaru
        info(f"Berhasil, username {userbaru} telah terdaftar")
    except ValueError as e:
        print(e)

while True:
    os.system("cls || clear")
    print("TOKO PENYEWAAN ALAT CAMPING \n1. registrasi \n2. Login \n3. Keluar")
    menu = input("pilih menu (1/2/3/4): ")
    os.system("cls || clear")

    if menu == "1":
        registrasi()
        input("enter untuk kembali ke menu....")

    elif menu == "2":
        status = login()

    elif menu == "3":
        input("enter untuk keluar...")
        break
    else:
        print("!!!!! pilihan tidak valid, coba lagi !!!!!".center(50))
        input("enter untuk kembali ke menu....")
        
os.system('cls || clear')
print("ANDA TELAH KELUAR".center(50))
print("TERIMA KASIH SUDAH MENGGUNAKAN PROGRAM INI".center(50))
exit