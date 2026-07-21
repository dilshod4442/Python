son = int(input("Juft son kiriting: "))

if son % 2 == 0:
    print("Rahmat!")
else:
    print("Bu son juft emas.")


yosh = int(input("Yoshingiz nechida? "))

if yosh < 4:
    price = 0
elif yosh < 18:
    price = 10000
elif yosh <= 60:
    price = 20000
elif yosh > 60:
    price = 0

print(f"Sizga kirish {price} so'm")

son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))

if son1 > son2:
    print(f"{son1}>{son2}")
elif son1 < son2:
    print(f"{son1}<{son2}")
else:
    print(f"{son1}={son2}")

foydalanuvchilar = ["dilshod", "ali", "vali", "sardor", "aziz"]

login = input("Yangi login kiriting: ")

if login.lower() in foydalanuvchilar:
    print("Login band, yangi login tanlang!")
else:
    print(f"Xush kelibsiz, {login}!")

son = int(input("Butun son kiriting: "))

for i in range(2, 11):
   if son % i == 0:
     print(f"{i} ga qoldiqsiz bo'linadi")


python_lugat = {
    "Boolean": "Mantiqiy qiymat",
    "Float": "O'nlik son",
    "For": "Takrorlash tsikli",
    "If": "Shart operatori",
    "Integer": "Butun son",
    "List": "Ro'yxat",
    "Dictionary": "Lug'at",
    "Tuple": "O'zgarmas ro'yxat",
    "String": "Matn",
    "While": "Takrorlash tsikli"
}

for kalit in sorted(python_lugat):
    print(f"{kalit} - {python_lugat[kalit]}")

davlatlar = {
    "O'zbekiston": "Toshkent",
    "AQSh": "Washington D.C.",
    "Rossiya": "Moskva",
    "Qozog'iston": "Nursulton",
    "Qirg'iziston": "Bishkek",
    "Tojikiston": "Dushanbe",
    "Italiya": "Rim",
    "Malayziya": "Kuala-Lumpur",
    "Singapur": "Singapur"
}

print("Dunyo davlatlari:")
for davlat in sorted(davlatlar):
    print(davlat)

print("\nDavlatlarning poytaxtlari:")
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt)


davlatlar = {
    "O'zbekiston": "Toshkent",
    "AQSh": "Washington D.C.",
    "Rossiya": "Moskva",
    "Qozog'iston": "Nursulton",
    "Qirg'iziston": "Bishkek",
    "Tojikiston": "Dushanbe",
    "Italiya": "Rim",
    "Malayziya": "Kuala-Lumpur",
    "Singapur": "Singapur"
}

davlat = input("Qaysi davlatning poytaxtini bilishni istaysiz? ")

abu_abdulloh = {
    "ism": "Abu Abdulloh Muhammad ibn Ismoil",
    "t_yil": 810,
    "joy": "Buxoro",
    "umr": 60
}

abdulla_qodiriy = {
    "ism": "Abdulla Qodiriy",
    "t_yil": 1894,
    "joy": "Toshkent",
    "umr": 44
}

erkin_vohidov = {
    "ism": "Erkin Vohidov",
    "t_yil": 1936,
    "joy": "Farg'ona",
    "umr": 80
}

alisher_navoiy = {
    "ism": "Alisher Navoiy",
    "t_yil": 1441,
    "joy": "Xirot",
    "umr": 60
}

mashhurlar = [
    abu_abdulloh,
    abdulla_qodiriy,
    erkin_vohidov,
    alisher_navoiy
]

for odam in mashhurlar:
    print(
        f"{odam['ism']} {odam['t_yil']}-yilda "
        f"{odam['joy']}da tavallud topgan. "
        f"{odam['umr']} yil umr ko'rgan."
    )


mashhurlar = {
    "Abu Abdulloh Muhammad ibn Ismoil": {
        "tugilgan": 810,
        "joy": "Buxoro",
        "umr": 60,
        "asarlar": [
            "Al-jome' as-sahih",
            "Al-adab al-mufrad",
            "At-tarix al-kabir",
            "At-tarix as-sag'ir"
        ]
    },

    "Abdulla Qodiriy": {
        "tugilgan": 1894,
        "joy": "Toshkent",
        "umr": 44,
        "asarlar": [
            "O'tkan kunlar",
            "Mehrobdan Chayon",
            "Obid ketmon"
        ]
    },

    "Erkin Vohidov": {
        "tugilgan": 1936,
        "joy": "Farg'ona",
        "umr": 80,
        "asarlar": [
            "Tong nafasi",
            "Qo'shiqlarim sizga",
            "O'zbegim",
            "Qiziquvchan Matmusa"
        ]
    },

    "Alisher Navoiy": {
        "tugilgan": 1441,
        "joy": "Xirot",
        "umr": 60,
        "asarlar": [
            "Xamsa",
            "Lison ut-Tayr",
            "Mahbub Al-Qulub",
            "Munojot"
        ]
    }
}

# 1-qism
for ism, info in mashhurlar.items():
    print(f"{ism} {info['tugilgan']}-yilda {info['joy']}da tavallud topgan.")
    print(f"{info['umr']} yil umr ko'rgan.\n")

# 2-qism
for ism, info in mashhurlar.items():
    print(f"{ism} ning mashhur asarlari:")
    for asar in info["asarlar"]:
        print(asar)
    print()

kitoblar = []

while True:
    kitob = input("Yaxshi ko'rgan kitobingizni kiriting (stop - chiqish): ")

    if kitob.lower() == "stop":
        break

    kitoblar.append(kitob)

print("\nKiritilgan kitoblar:")
for kitob in kitoblar:
    print(kitob)

while True:
    yosh = input("Yoshingizni kiriting (exit  chiqish): ")

    if yosh.lower() in ["exit"]:
        break

    yosh = int(yosh)

    if yosh < 7:
        narx = 2000
    elif yosh <= 18:
        narx = 3000
    elif yosh <= 65:
        narx = 10000
    else:
        narx = 0

    if narx == 0:
        print("Kirish bepul")
    else:
        print(f"Chipta narxi: {narx} so'm")