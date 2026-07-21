# Проверка email

pochta = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]

for email in pochta:
    if "@" in email:
        print(email)
    else:
        print("Noto'g'ri email:", email)


# Проверка паролей

parollar = ["password123", "Qwerty!", "admin", "StrongPass1!"]

for parol in parollar:
    if len(parol) < 8:
        print(parol, "Juda qisqa")
    else:
        if parol.isalpha():
            print(parol, "Kuchsiz parol")
        else:
            print(parol, "Kuchli parol")


# Температура

haroratlar = [20, 22, 19, 24, 25, 23, 21]

jami = 0

for harorat in haroratlar:
    jami += harorat

    if harorat > 22:
        print("Iliq kun")
    else:
        print("Salqin kun")

print("O'rtacha:", jami / len(haroratlar))


# Заказ еды

taomlar = ["Osh", "Shashlik", "Manti", "Lag'mon"]

buyurtma = input("Taom kiriting: ")

for taom in taomlar:
    if buyurtma == taom:
        print("Buyurtmangiz qabul qilindi")
        break
else:
    print("Kechirasiz, bunday taom yo'q")


# Проверка возраста

yoshlar = [16, 21, 17, 30, 25]

for yosh in yoshlar:
    if yosh < 18:
        print("Yosh chegarasiga yetmagan")
    else:
        print("Xush kelibsiz")


# Сообщения

xabarlar = ["Yangi xabar", "Batareya past", "Yangilanish mavjud"]

for xabar in xabarlar:
    if xabar == "Batareya past":
        print("Telefoningizni quvvatlang")


# Разделение файлов

fayllar = [
    "kitob.jpg",
    "ko_jiguli.mp3",
    "tabiat.jpg",
    "malohat.mp3",
    "iphone16.jpg"
]

musiqalar = []
rasmlar = []

for fayl in fayllar:
    if ".jpg" in fayl:
        rasmlar.append(fayl)

    if ".mp3" in fayl:
        musiqalar.append(fayl)

print(rasmlar)
print(musiqalar)