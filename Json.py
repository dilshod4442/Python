import json

data = {
    "model": "Malibu",
    "Rang": "Qora",
    "Yil": 2020,
    "Narh":40000
}
data1 = json.dumps(data, indent=3)
print(data1)



talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""

talaba = json.loads(talaba_json)

print(talaba["ism"], talaba["familiya"])

with open("data.txt", "w") as f:
     json.dump(data,f, indent=4)


with open("datas.txt", "w") as f:
    json.dump(data1,f, indent=4)


with open("students.json", "r") as f:
    data = json.load(f)

for talaba in data["student"]:
    print(f"{talaba['name']} {talaba['lastname']}, {talaba['year']}-kurs, {talaba['faculty']} talabasi")


with open("api.php.json", "r") as api:
    a = json.load(api,)

for api in a["query"]["pages"].values():
    print(f"{api['title']} {api['extract']}")
