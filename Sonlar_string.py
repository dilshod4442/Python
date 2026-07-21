kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzoi"
viloyat="samarqand"
bog_mah = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(bog_mah)

kocha = input("Ko'cha nomini kiriting: ")
mahalla = input("Mahalla nomini kiriting: ")
tuman = input("Tuman nomini kiriting: ")
viloyat = input("Viloyat nomini kiriting: ")
manzil = f"{kocha} ko'chasi,\n{mahalla} mahallasi,\n{tuman} tumani,\n{viloyat} viloyati"
print(manzil)

print(manzil.lower())
print(manzil.upper())
print(manzil.capitalize())
print(manzil.title())



yil = input("Tugulgan yiligizni kiriting?")
Yosh = 2026 - int(yil)
print("siz " + str(Yosh) + " ekansiz")


son = int(input("Istalgan son kiriting: "))

print(f"{son} ning kvadrati {son ** 2} ga teng")
print(f"{son} ning kubi {son ** 3} ga teng")


birinchi = int(input("Birinchi sonni kiriting: "))
ikkinchi = int(input("Ikkinchi sonni kiriting: "))

print(f"{birinchi} + {ikkinchi} = {birinchi + ikkinchi} ")
print(f"{birinchi} - {ikkinchi} = {birinchi - ikkinchi} ")
print(f"{birinchi} * {ikkinchi} = {birinchi * ikkinchi} ")
print(f"{birinchi} / {ikkinchi} = {birinchi / ikkinchi} ")