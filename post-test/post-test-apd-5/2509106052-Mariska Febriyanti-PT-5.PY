from tabulate import tabulate
import os
login_admin = True
login_user = True
anggota = []
list_barang=[
    ["tenda 2 orang banyak","10","50000","tersedia"],
    ["kursi lipat","15","15000","tersedia"],
    ["meja lipat","8","10000","tersedia"]
]
baris1 = "^"*50
baris2 = "="*50
baris3 = "~"*50
baris4 = "_"*50

while True:
    os.system("cls")
    print("TOKO PENYEWAAN ALAT CAMPING \n1. admin \n2. pengguna biasa \n3. Registrasi  \n4. Keluar")
    menu = input("pilih menu (1/2/3/4): ")
    os.system("cls")

    if menu == "1":
        print(baris2)
        print("LOGIN SEBAGAI ADMIN".center(50))
        print(baris2)
        user = input("username: ")
        pw = input("password: ")
        if user == "kemping" and pw == "gas":
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
        if user in anggota and pw in anggota:
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
        usn_baru = input("Username: ")
        pw_baru = input("Password: ")
        anggota.append(usn_baru)
        anggota.append(pw_baru)
        print(baris3)
        print(f"Berhasil, username {usn_baru} telah terdaftar".center(50))
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
            os.system("cls")
            print("SILAHKAN PILIH OPSI")
            print("1. Lihat barang \n2. sewa barang \n3. keluar")
            menu_user = input("masukkan pilihan (1/2/3): ")
            os.system("cls")
            if menu_user == "1":
                print(baris2)
                print("DAFTAR BARANG".center(50))
                print(baris2)
                if len(list_barang) == 0:
                    print(baris1)
                    print("belum ada barang tersedia".center(50))
                    print(baris1)
                    input("enter untuk kembali ke menu....")
                else:
                    list_data=[]
                    for i,b in enumerate(list_barang):
                        if b[1] == 0:
                            b[3] = "habis"
                        else:
                            b[3] = "tersedia"
                        barang = b[0], b[1], b[2], b[3]
                        list_data.append([i+1.] + list(barang))
                    headers = ["no", "nama barang", "stok", "harga", "status"]
                    print(tabulate(list_data, headers=headers, tablefmt="pipe"))
                    input("enter untuk kembali ke menu....")
            elif menu_user == "2":
                print(baris2)
                print("PENYEWAAN BARANG".center(50))
                print(baris2)
                if len(list_barang) == 0:
                    print(baris1)
                    print("belum ada barang tersedia".center(50))
                    print(baris1)
                    input("enter untuk kembali ke menu....")
                else:
                    list_data=[]
                    for i,b in enumerate(list_barang):
                        barang = b[0], b[1], b[2], b[3]
                        list_data.append([i+1.] + list(barang))
                    headers = ["no", "nama barang", "stok", "harga", "status"]
                    print(tabulate(list_data, headers=headers, tablefmt="pipe"))
                    pilih = int(input("masukkan nomor barang yang ingin di sewa: "))
                    print(baris4)
                    barang = list_barang[pilih-1]
                    jumlah = int(input("jumlah barang yang di sewa: "))
                    print(baris4)
                    stok_awal = int(barang[1])
                    if jumlah > stok_awal:
                        print("!!!!! stok tidak mencukupi !!!!!".center(50))
                        input("enter untuk kembali ke menu....")
                    else:
                        stok_baru = stok_awal - jumlah
                        barang[1] = stok_baru
                        print(f"anda menyewa {jumlah} {barang[0]}")
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
            os.system("cls")
            print("SILAHKAN PILIH OPSI")
            print("1. Tambah Barang \n2. Lihat barang \n3. Perbarui barang \n4. Hapus Barang \n5. Keluar")
            menu_admin = input("masukkan pilihan (1/2/3/4/5): ")
            os.system("cls")
            if menu_admin == "1":
                print(baris2)
                print("MENAMBAHKAN BARANG".center(50))
                print(baris2)
                barang =  input("Nama barang: ")
                stok = input("Stok: ")
                harga = input("Harga: ")
                status = input("Status: ")
                list_barang.append([barang,stok,harga,status])
                print(baris3)
                print(f"{barang} berhasil ditambahkan".center(50))
                print(baris3)
                input("enter untuk kembali ke menu....")

            elif menu_admin == "2":
                print(baris2)
                print("DAFTAR BARANG".center(50))
                print(baris2)
                if len(list_barang) == 0:
                    print(baris1)
                    print("belum ada barang tersedia".center(50))
                    print(baris1)
                    input("enter untuk kembali ke menu....")
                else:
                    list_data=[]
                    for i,b in enumerate(list_barang):
                        barang = b[0], b[1], b[2], b[3]
                        list_data.append([i+1.] + list(barang))
                    headers = ["no", "nama barang", "stok", "harga", "status"]
                    print(tabulate(list_data, headers=headers, tablefmt="pipe"))
                    input("enter untuk kembali ke menu....")

            elif menu_admin == "3":
                print(baris2)
                print("PERBARUI BARANG".center(50))
                print(baris2)
                if len(list_barang) == 0:
                    print(baris1)
                    print("belum ada barang tersedia".center(50))
                    print(baris1)
                    input("enter untuk kembali ke menu....")
                else:
                    list_data=[]
                    for i,b in enumerate(list_barang):
                        barang = b[0], b[1], b[2], b[3]
                        list_data.append([i+1.] + list(barang))
                    headers = ["no", "nama barang", "stok", "harga", "status"]
                    print(tabulate(list_data, headers=headers, tablefmt="pipe"))
                    pilih = int(input("masukkan nomor yang mau diperbarui: "))
                    barang = list_barang[pilih-1]
                    print("ENTER jika tidak ingin merubah nilai")
                    print(baris4)
                    nama_baru = input("nama barang: ")
                    stok_baru = input("stok: ")
                    harga_baru = input("harga: ")
                    status_baru = input("status: ")
                    if nama_baru != "":
                        barang[0]=nama_baru
                    elif stok_baru != "":
                        barang[1]=stok_baru
                    elif harga_baru != "":
                        barang[2]=harga_baru
                    elif status_baru != "":
                        barang[3]=status_baru
                    print(baris3)
                    print("barang berhasil di perbarui".center(50))
                    print(baris3)
                    input("enter untuk kembali ke menu....")

            elif menu_admin == "4":
                print(baris2)
                print("MENGHAPUS BARANG".center(50))
                print(baris2)
                if len(list_barang) == 0:
                    print(baris1)
                    print("belum ada barang tersedia".center(50))
                    print(baris1)
                    input("enter untuk kembali ke menu....")
                else:
                    list_data=[]
                    for i,b in enumerate(list_barang):
                        barang = b[0], b[1], b[2], b[3]
                        list_data.append([i+1.] + list(barang))
                    headers = ["no", "nama barang", "stok", "harga", "status"]
                    print(tabulate(list_data, headers=headers, tablefmt="pipe"))
                    pilih = int(input("masukkan nomor yang ingin dihapus: "))
                    del list_barang[pilih-1] 
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
        os.system('cls')
        print(baris3)
        print("ANDA TELAH KELUAR".center(50))
        print("TERIMA KASIH SUDAH MENGGUNAKAN PROGRAM INI".center(50))
        print(baris3)
        break