matn = input("Matnni kiriting: ")
soz = input("Qidirilayotgan so‘zni kiriting: ")
boshlanish = int(input("Qidirishni qayerdan boshlaymiz (indeks): "))

indeks = matn.find(soz, boshlanish)

print(indeks)