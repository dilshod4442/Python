import pickle
fayl = open("math.txt")
pi = fayl.read()
print(pi)
fayl.close()

def tekshir_sana(kun, oy, yil):
    sana = f"{kun}{oy}{yil}"

    with open("pi_million_digits.txt", "r") as file:
        pi = file.read()

    if sana in pi:
        print(f"{sana} soni PI ichida bor.")
    else:
        print(f"{sana} soni PI ichida yo'q.")


tekshir_sana(25, 2, 2000)



with open("pickle,txt", "r") as file:
    son = float(file.read())

with open("math.pkl", "wb") as file:
    pickle.dump(son,file)

faylnomi = "malumotlar.txt"

with open("malumotlar.txt", "a") as file:

  while True:
    malumotlar = input("Ma'lumot kiriting (toxtatish uchun 'stop'): ")

    if malumotlar.lower() == "stop":
        break

    if malumotlar.strip() == "":
        continue

    file.write(malumotlar + "\n")

print("saqlandi")