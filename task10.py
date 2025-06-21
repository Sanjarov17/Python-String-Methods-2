matn = input("Matnni kiriting: ")
soz = input("Qidirilayotgan so‘zni kiriting: ")

indeks = matn.find(soz)

print(indeks)
if matn.find(soz) == -1:
    print("So‘z topilmadi")
else:
    print("So‘z topildi")
