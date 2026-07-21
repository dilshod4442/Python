# radius = float(input("Doiraning radiusini kiriting(sm):"))
# l = 2*3.14*radius
# s = 2*3.14*(radius**2)
#
# print(f"Doiraning yuzi {s} sm kvadratga, uzunligi {l} sm ga, radiusi {radius} sm ga teng. ")

def doira(radius):
    pi = 3.14
    doira_params = {
        "uzunlik":2*pi*radius,
        "yuzi": 2*pi*(radius**2),
        "radiusi":radius
    }
    return doira_params

doira1 = doira(12)
print(doira1)

# def tubmi(son):
#     k=0
#     for i in range(1,son+1):
#         if son % i == 0:
#             k+=1
#     if k==2:
#         print("tub son")
#     else:
#         print("tub emas")
#
# tubmi(73)

# def tub_sonlar(boshlanish, tugash):
#     natija = []
#
#     for son in range(boshlanish, tugash + 1):
#         if son < 2:
#             continue
#
#         tub = True
#         for i in range(2, int(son ** 0.5) + 1):
#             if son % i == 0:
#                 tub = False
#                 break
#
#         if tub:
#             natija.append(son)
#
#     return natija
#
#
# # Misol
# print(tub_sonlar(10, 50))

def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    """Avtomobil haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto

def avto_kirit():
    """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bitta ro'yxatga joylash imkonini beruvchi funksiya"""
    avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting",end='')
        kompaniya=input("Ishlab chiqaruvchi: ")
        model=input("Modeli: ")
        rangi=input("Rangi: ")
        korobka=input("Korobka: ")
        yili=input("Ishlab chiqarilgan yili: ")
        narhi=input("Narhi: ")
        #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida
        #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
        avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
        # Yana avto qo'shish-qo'shmaslikni so'raymiz
        javob = input("Yana avto qo'shasizmi? (yes/no): ")
        if javob=='no':
            break
    return avtolar

def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
    print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
          f"{avto_info['yil']}-yil, {avto_info['narh']}$")