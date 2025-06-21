matn = input("Matnni kiriting: ")
harf = input("Qaysi harfni sanaymiz: ")

sanoq = matn.count(harf)

print(sanoq)
if matn.count(harf):
    print("harf topildi")
else:
    print("harf topilmadi")


