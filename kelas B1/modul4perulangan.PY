for ulang in range (5):
    print(f"ini angka {ulang} ")

for i in range (10):
    print("-", end = ".")

print("*")
for i in range(5):
    for j in range(i+1):
        print("*", end= "_")
    print()

for i in range(0, 4):
    for j in range(0, 5):
        print(f'{i} x {j} = {i * j}', end= " ")
    print('')

dompet = [1, 2, 3, 4]
panjang = len(dompet)
for i in range(len(panjang)):
    print(dompet[i])

i = 5
while i < 10:
    i = i + 1
    print (i)

username = input("masukkan username: ")
while username == "":
    username = input("masukkin woy: ")

