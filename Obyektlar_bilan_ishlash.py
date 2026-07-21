class User:
    """Foydalanuvchi klassi"""

    def __init__(self, ism, familiya, username, email, telefon):
        self.ism = ism
        self.familiya = familiya
        self.username = username
        self.email = email
        self.telefon = telefon

    def get_info(self):
        """Foydalanuvchi haqida ma'lumot"""
        return (f"Foydalanuvchi: {self.username}, "
                f"Ismi: {self.ism} {self.familiya}, "
                f"Email: {self.email}, "
                f"Telefon: {self.telefon}")



# Obyektlar
user1 = User("Alijon","Valiyev","Alijon_Valiyev", "alijon1994@gmail.com", "+998097435567")
user2 = User("Dilshod", "Karimov", "dilshod_Karimov", "dilshod@gmail.com", "+998991234567")
user3 = User("Aziza", "Rahimova", "aziza_Rahimov", "aziza@gmail.com", "+998933334455")
print(user1.get_info())
print(user2.get_info())
print(user3.get_info())


class Avto:

    def __init__(self,model,rang,korobka,narx,yil,kilometr=0):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narx = narx
        self.yil = yil
        self.kilometr = kilometr

    def get_info(self):
        return f"{self.model}, {self.rang}, {self.narx}$, {self.yil}, {self.kilometr} km"

    def update_km(self, km):
        self.kilometr += km


class Avtosalon:

    def __init__(self, nomi, manzil):
        self.nomi = nomi
        self.manzil = manzil
        self.avtolar = []
        self.avtolar_soni = 0

    def add_avto(self, avto):
        self.avtolar.append(avto)
        self.avtolar_soni += 1

    def get_avtolar(self):
        return [avto.get_info() for avto in self.avtolar]

avto1 = Avto("Malibu 2","Qora","Avtomat",32000, 2017)
avto2 = Avto("Cobalt","Oq","Avtomat", 13000,2026)
avto3 = Avto("Tracker", "Oq", "Avtomat", 26000, 2025)


salon = Avtosalon("GM Motors", "Toshkent")

salon.add_avto(avto1)
salon.add_avto(avto2)
salon.add_avto(avto3)

print(salon.avtolar_soni)
print(salon.get_avtolar())

print(dir(Avto))
print(dir(avto1))

print(dir(Avtosalon))
print(dir(salon))

print(avto1.__dict__)
print(salon.__dict__)
print(dir(str))
print(dir(int))