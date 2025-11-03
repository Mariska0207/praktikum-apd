from prettytable import PrettyTable
import os
import inquirer

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

def daftarbarang():
    jumlahbarang(barang)
    for i, j in barang.items():
        if j["stok"] == 0:
            j["status"] = "habis"
        else:
            j["status"] = "tersedia"
    table = PrettyTable()
    table.field_names = ["No","Nama barang", "stok", "harga", "status"]
    for i,j in barang.items():
        table.add_row([i,j["nama barang"], j["stok"], j["harga"], j["status"]])
    print(table)
    print(f"jumlah barang tersedia: {jumlahtersedia()}\n")

def totalbayar(harga,jumlah):
    total = harga * jumlah
    print(f"total bayar: Rp {total}")
    return total

def sewabarang():
    daftarbarang()
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

def loginuser():
    while True:
        os.system("cls || clear")
        menuuser = [
            inquirer.List("opsi",
                    message="SILAHKAN PILIH OPSI",
                    choices=["1.lihat barang", "2.sewa barang", "3.keluar"],
                ),
        ]
        answer = inquirer.prompt(menuuser)
        menuuser = answer["opsi"]
        os.system("cls || clear")

        if "1" in menuuser:
            judul("DAFTAR BARANG")
            daftarbarang()
            input("enter untuk kembali ke menu....")
        elif "2" in menuuser:
            judul("PENYEWAAN BARANG")
            sewabarang()
            input("enter untuk kembali ke menu....")

        else:
            break