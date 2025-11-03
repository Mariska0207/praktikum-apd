import inquirer
import os
from user import judul,info,barang,daftarbarang

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
    daftarbarang()
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
    daftarbarang()
    try:
        pilih = int(input("masukkan nomor yang ingin dihapus: "))
        key = list(barang.keys())[pilih-1]
        del barang[key]
        info("barang berhasil di hapus")
    except (ValueError,IndexError):
        print("!!!!! Kesalahan inputan. Silakan coba lagi. !!!!!".center(50))


def loginadmin():
    while True:
        os.system("cls || clear")
        menuadmin = [
            inquirer.List("opsi",
                    message="SILAHKAN PILIH OPSI",
                    choices=["1.tambahbarang", "2.lihat barang", "3.perbarui barang", "4.hapus barang", "5.keluar"],
                ),
        ]
        answer = inquirer.prompt(menuadmin)
        menuadmin = answer["opsi"]
        os.system("cls || clear")

        if "1" in menuadmin:
            judul("MENAMBAHKAN BARANG")
            tambahbarang()
            input("enter untuk kembali ke menu....")

        elif "2" in menuadmin:
            judul("DAFTAR BARANG")
            daftarbarang()
            input("enter untuk kembali ke menu....")

        elif "3" in menuadmin:
            judul("PERBARUI BARANG")
            perbaruibarang()
            input("enter untuk kembali ke menu....")

        elif "4" in menuadmin:
            judul("MENGHAPUS BARANG")
            hapusbarang()
            input("enter untuk kembali ke menu....")

        else:
            break

