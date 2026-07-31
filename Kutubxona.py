import datetime as dt
import re

bugun = dt.date.today()

for i in range(10):
    sana = bugun + dt.timedelta(i * 14)
    print(sana)

hozir = dt.datetime.now()
Ramozon = dt.datetime(2027,3,10)
qoldi = Ramozon - hozir
kunlar = qoldi.days
print(f"Ramazon hayitiga: {kunlar} kun qoldi")


hozir = dt.datetime.now()
Qurbon = dt.datetime(2027,5,17)
qoldi = Qurbon - hozir
kunlar = qoldi.days
print(f"Qurbon hayitiga: {kunlar} kun qoldi")


def yosh():
    tugilgan = dt.date(2010, 9, 18)
    bugun = dt.date.today()

    farq = bugun - tugilgan

    print("Tug'ilgan kunimdan o'tgan kun:", farq.days)

yosh()


telefon = input("Telefon raqamini kiriting: ")

andoza = r"^\+998\d{9}$"

if re.match(andoza, telefon):
    print(f"Telefon raqamingiz: {telefon}")
else:
    print("Telefon raqami noto'g'ri")



def sayt_ajrat(math):
    andoza = r"https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)"
    return re.findall(andoza,math)

matn = """
Salom, Aziz!

Konferensiya haqida batafsil ma'lumotni https://conference2026.org saytidan ko'rishingiz mumkin.
Ro'yxatdan o'tish uchun https://conference2026.org/register havolasidan foydalaning.
Savollaringiz bo'lsa, biz bilan bog'laning.

Yaxshi kun tilaymiz!
"""

print(sayt_ajrat(matn))