# praktikum = ["Mahasiswa", 20, True, 45.10, ["APD",25]]
# print(praktikum[-1][0])

# list_random = ["Mahasiswa", 20, True, 45.10, ["APD",25]]
# list_random.append("bang riyadi")
# print(list_random)
# list_random.insert(3, ["unmul", "smd"])
# print(list_random)
# list_random[1]= "Mariska"
# print(list_random)
# del list_random[3]
# print(list_random)
# list_random[-1][1] = "rusia"
# print(list_random)
# hilang = list_random.pop(3)
# print(list_random)
# print(hilang)
# hilang = list_random.pop(1)
# print(list_random)
# print(hilang)
# list_random[4].pop(0)
# print(list_random)
# print(list_random[0:4:1])
# for i in range(len(list_random)):
#     print(i+1,list_random[i])
# kelas = ["ahnaf",2,3]
# # hasil=kelas+list_random
# # print(hasil)
# for i in kelas:
#     print(i*2)
# kelas = [
#     ["Ridho", "Lian", "Nabil"],
#     ["Daffa", "Dante", "Santoso"],
#     ["Pernanda", "Riyadi", "Ahnaf"],
# ]
# print(kelas[-1][-1])

anggota = ("riyadi", 20, True, 3.96, ["APD",25],("samarinda",12))
# print(anggota)
for i in anggota:
    print(i)

langgota=list(anggota)
os.system('cls')
print(langgota)
langgota.remove("riyadi")
print(langgota)
anggota=tuple(langgota)
print(anggota)
import os
tugas = ('rangkuman', 'arduino','scrapping')
(PTI, orsikom, basisdata) = tugas
print(PTI)
print(orsikom)
print(basisdata)