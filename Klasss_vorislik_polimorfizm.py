class Shaxs:
    odamlar_soni = 0

    def __init__(self, ism, familiya, passport, tyil):
        self.__ism = ism
        self.__familiya = familiya
        self.__passport = passport
        self.__tyil = tyil
        Shaxs.odamlar_soni += 1

    def get_ism(self):
        return self.__ism

    def set_ism(self, ism):
        self.__ism = ism

    def get_familiya(self):
        return self.__familiya

    def set_familiya(self, familiya):
        self.__familiya = familiya

    def get_passport(self):
        return self.__passport

    def set_passport(self, passport):
        self.__passport = passport

    def get_tyil(self):
        return self.__tyil

    def set_tyil(self, tyil):
        self.__tyil = tyil

    def get_info(self):
        return f"{self.__ism} {self.__familiya}. Passport: {self.__passport}, {self.__tyil}-yilda tug'ilgan"

    def get_age(self, yil):
        return yil - self.__tyil

    @classmethod
    def odamlar_sonini_korsat(cls):
        return f"Jami odamlar: {cls.odamlar_soni}"


class Manzil:
    def __init__(self, uy, kocha, tuman, viloyat):
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat

    def get_manzil(self):
        return f"{self.viloyat} viloyati, {self.tuman} tumani, {self.kocha} ko'chasi, {self.uy}-uy"


class Fan:
    def __init__(self, nomi):
        self.__nomi = nomi

    def get_nomi(self):
        return self.__nomi


class Talaba(Shaxs):
    talabalar_soni = 0

    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []
        Talaba.talabalar_soni += 1

    def get_id(self):
        return self.idraqam

    def get_bosqich(self):
        return self.bosqich

    def fanga_yozil(self, fan):
        self.fanlar.append(fan)

    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            print("Siz bu fanga yozilmagansiz")

    def get_info(self):
        fanlar = [fan.get_nomi() for fan in self.fanlar]
        return f"{super().get_info()}, ID: {self.idraqam}. Bosqich: {self.bosqich}, Fanlar: {fanlar}"

    @classmethod
    def talabalar_sonini_korsat(cls):
        return f"Jami talabalar: {cls.talabalar_soni}"


class Professor(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, fan):
        super().__init__(ism, familiya, passport, tyil)
        self.fan = fan

    def get_info(self):
        return f"{super().get_info()}, Fan: {self.fan}"


class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, login):
        super().__init__(ism, familiya, passport, tyil)
        self.login = login

    def get_info(self):
        return f"{super().get_info()}, Login: {self.login}"


class Sotuvchi(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, dokon):
        super().__init__(ism, familiya, passport, tyil)
        self.dokon = dokon

    def get_info(self):
        return f"{super().get_info()}, Dokon: {self.dokon}"


class Mijoz(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, balans):
        super().__init__(ism, familiya, passport, tyil)
        self.balans = balans

    def get_info(self):
        return f"{super().get_info()}, Balans: {self.balans}"


class Admin(Foydalanuvchi):
    def ban_user(self):
        print("Foydalanuvchi bloklandi")



manzil = Manzil(12, "olmazor", "Bogbon", "Samarqand")

talaba = Talaba("Valijon", "Aliyev", "FA112229", 2000, "0000012", manzil)

matematika = Fan("Matematika")
fizika = Fan("Fizika")

talaba.fanga_yozil(matematika)
talaba.fanga_yozil(fizika)

print(talaba.get_info())
print(talaba.manzil.get_manzil())

admin = Admin("Ali", "Karimov", "AA12356", 1998, "admin01")

print(admin.get_info())
admin.ban_user()

print(talaba.talabalar_sonini_korsat())
print(Shaxs.odamlar_sonini_korsat())