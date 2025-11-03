from user import judul,info,loginuser
from admin import loginadmin
kesempatanlogin = 3
anggota = {
    "user": "mar",
    "pw": "052"
}

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