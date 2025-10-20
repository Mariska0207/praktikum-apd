# SET
buah = {"apel", "jeruk", "mangga"}
# sayur = {"bayam", "kangkung", "sawi"}
buah1 = {"anggur","apel", "semangka", "ceri"}
# set_all = buah.update(buah1)
# set_all = buah.union(buah1)
# set_all = buah.intersection(buah1)
# set_all = buah.difference(buah1)
print(set_all)
# buah.add("semangka")
# print(buah)
# buah.remove("apel")
# print(buah)
# buah.discard("anggur")
# print(buah)

# DICTIONARY
# memakai titik dua(:) bukan sama dengan(=)
# Daftar_buku = {
# "Buku1" : "Bumi Manusia",
# "Buku2" : "Laut Bercerita"
# }
# print(Daftar_buku["Buku1"])
# print(Daftar_buku)

# Biodata = {
#     "Nama" : "Mariska Febriyanti",
#     "umur" : 18,
#     "NIM" : "2409106050",
#     "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" : True,
#     "Social Media" : {"Instagram" : "daffahrhap",
#     }
# }
# print(Biodata["KRS"][1])
# print(f"nama saya adalah {Biodata['Nama']}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# print(f"nama saya adalah {Biodata.get['Nama']}")
# print(Biodata.get('Nama'))

# Nilai = {
#     "Matematika": 80,
#     "B. Indonesia": 90,
#     "B. Inggris": 81,
#     "Kimia": 78,
#     "Fisika": 80
# }
# # Tanpa menggunakan items()
# for i in Nilai:
#     print(i)
# print("") # pemisah
# # Menggunakan items()
# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")

# Film = {
#     "Avenger Endgame" : "Action",
#     "Sherlock Holmes" : "Mystery",
#     "The Conjuring" : "horror"
#     }
# #Sebelum Ditambah
# print(Film)
# Film["Zombieland"] = "Comedy" #cara 1
# Film.update({"Hours" : "Thriller"}) #cara2(bisa nambah sekali banyak)
# #Setelah Ditambah
# print(Film)

# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "kimia" : 95
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)

# Musik = {
#     "The Chainsmoker" : ["All we Know", "The Paris"],
#     "Alan Walker" : ["Alone", "Lily"],
#     "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
#     print("")