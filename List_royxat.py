# 1 capitalize()  Converts the first character to upper case
from posixpath import join

# cap = "capitalize"
# print(cap.capitalize())
# cap2 = "olma"
# print(cap2.capitalize())

# 2 casefold()  Converts string into lower case

# case = 'caseEE'
# print(case.casefold())
#
# case2 = "cases"
# print(case2.casefold())

# 3 center()  Returns a centered string
# txt = "banana"
# x = txt.center(200)
# print(x)
#
# txt1 = "orta"
# x = txt1.center(50)
# print(x)

# 4 count()  Returns the number of times a specified value occurs in a string

# count = ["Count", "Apple", "cherry", "Count"]
# print(count.count("Count"))
# print(count.count("Apple"))
# print(count.count("cherry"))

# count2 = ["Olma", "Anjir", "cherry", "Olma"]
# print(count2.count("Olma"))
# print(count2.count("Anjir"))
# print(count2.count("cherry"))

# 5 encode()  Returns an encoded version of the string

# txt = "My name is Ståle"
# x = txt.encode()
# print(x)
#

# tx2 = "hello byteså"
# print(tx2.encode())

# 6 endswith()  Returns true if the string ends with the specified valu

# txt = "Hello, welcome to my world"
#
# x = txt.endswith("world")
#
# print(x)

# txt = "Hello"
#
# print(txt.endswith("o"))
# print(txt.endswith("lo")
# print(txt.endswith("x"))

# 7 expandtabs()  Sets the tab size of the string

# txt = "Математика\t5\nФизика\t4\nИнформатика\t5"
#
# print(txt.expandtabs(23))
#
# expand = "H\te\tl\tl\to"
# print(expand.expandtabs(3))

# 8 find()  Searches the string for a specified value and returns the position of where it was found

# txt = "Hello, welcome to my world."
#
# x = txt.find("welcome")
#
# print(x)
#
# txt2 = "Hello Banana "
#
# x = txt2.find("Banana")
#
# print(x)

# 9 format()  Formats specified values in a string
# price = 49
# print(f"For only {price:.2f} dollars!")

# price2 = 68
# print(f"For only {price2:.0f} dollars!")

# 10 format_map() Formats specified values in a string
# person = {
#     "name": "Dilshod",
#     "age": 16
# }
#
# txt = "Меня зовут {name}, мне {age} лет"
#
# print(txt.format_map(person))
#
# PersonName = {
#     "Name": "Jonibek",
#     "Age": 27
# }
# txt2 = "Меня зовут {Name}. мне {Age} лет"
# print(txt2.format_map(PersonName))

# 11 index()  Searches the string for a specified value and returns the position of where it was found

# txt = "Hello, welcome to my world."
# x = txt.index("welcome")
# print(x)
#
# txt = "Hello world"
# print(txt.index("Hello"))

# 12 isalnum()  Returns True if all characters in the string are alphanumeric

# txt = "Company12@"
#
# x = txt.isalnum()
#
# print(x)
#
# txt = "Python12"
# x = txt.isalnum()
# print(x)
#
# 13 isalpha()  Returns True if all characters in the string are in the alphabet
# txt = "CompanyX"
#
# x = txt.isalpha()
#
# print(x)
# print("Hello123".isalnum())  # True
# print("Hello123".isalpha())  # False

# 14 isascii()  Returns True if all characters in the string are ascii characters

# txt = "Hello12d123"
# print(txt.isascii())
#
# txt2 = "привет"
# print(txt2.isascii())
# 15 isdecimal()  Returns True if all characters in the string are decimals
# txt = "12345"
# print(txt.isdecimal())
#
# txt = "123abc"
# print(txt.isdecimal())
# 16 isdigit()  Returns True if all characters in the string are digits
# txt = "50800"
#
# x = txt.isdigit()
#
# print(x)
# 17 isdigit() Returns True if all characters in the string are digits

# txt2 = "50800"
#
# x = txt.isdigit()
#
# print(x)
#
# txt2 = "50800ccdsa"
# print(txt.isdigit())
# 18  isidentifier()  Returns True if the string is an identifier
# txt = "11Demo1@@@@"
#
# x = txt.isidentifier()
#
# print(x)
#
# txt = "Demo"
#
# x = txt.isidentifier()
#
# print(x)
# 19 islower()  Returns True if all characters in the string are lower case
# txt = "hello world!"
#
# x = txt.islower()
#
# print(x)
#
# txt = "hellO world!"
#
# x = txt.islower()
#
# print(x)
#20isnumeric() Returns True if all characters in the string are numeric

# txt = "12345"
# print(txt.isnumeric())
#
# txt = "12345ВВ"
# print(txt.isnumeric())

# 20 isprintable()  Returns True if all characters in the string are printable
# txt = "Hello!"
# print(txt.isprintable())
#
# txt = "Hello\nWorld"
# print(txt.isprintable())

# 21 isspace()  Returns True if all characters in the string are whitespaces
# txt = "   "
# print(txt.isspace())
#
# txt = " qdqedqedqe  "
# print(txt.isspace())
# 22 istitle() Returns True if the string follows the rules of a title
# txt = "Hello World"
#
# print(txt.istitle())
#
# txt = "hello World"
#
# print(txt.istitle())
# 23 isupper()  Returns True if all characters in the string are upper case
# txt = "HELLO"
#
# print(txt.isupper())
#
# txt2 = "Hello"
# print(txt2.isupper())
# 24 join()  Joins the elements of an iterable to the end of the string

# words = ["Hello", "my", "friend"]
#
# x = " ".join(words)
#
# print(x)
#
# world = ["hello" , "my" , "friend"]
# x  = " ,".join(world)
# print(x)
# 25 ljust()  Returns a left justified version of the string
# txt = "Hello"
#
# x = txt.ljust(10)
#
# print(x)
#
# txt = "Hello"
#
# x = txt.ljust(120)
#
# print(x)

# txt = "Hello"
#
# x = txt.ljust(10, "-")
#
# print(x)
#26lower()  Converts a string into lower case
# txt = "Hello my FRIENDS"
#
# x = txt.lower()
#
# print(x)
# 27 lstrip()  Returns a left trim version of the string
# txt = "     Hello"
#
# print(txt.lstrip())
#
#
# txt = "    Hello    "
#
# print(txt.lstrip())
# 28 maketrans() Returns a translation table to be used in translations
# txt = "hello"
#
# table = str.maketrans("h", "H")
#
# print(txt.translate(table))
# 29 partition()  Returns a tuple where the string is parted into three parts
# txt = "Hello-World"
#
# x = txt.partition("-")
#
# print(x)
#
# email = "user@gmail.com"
#
# print(email.partition("@"))
# 32 replace()  Returns a string where a specified value is replaced with a specified value
# txt = "Hello world"
# x =  txt.replace("world", "Python")
# print(x)
#
# txt2 = "Apple mango "
# x = txt2.replace("mango", "Olma")
# print(x)
# 33 rfind()  Searches the string for a specified value and returns the last position of where it was found

# txt = "Hello hello hello"
#
# print(txt.find("hello"))
# print(txt.rfind("hello"))
#
# txt = "Python apple car"
# print(txt.find("apple"))
# print(txt.rfind("apple"))
# 34 rindex()  Searches the string for a specified value and returns the last position of where it was found
# txt = "Hello hello hello"
#
# print(txt.rindex("hello"))
# 35 rjust()  Returns a right justified version of the string
# txt = "banana"
#
# x = txt.rjust(20)
#
# print(x, "is my favorite fruit.")
#
# txt2 = "Aplle"
#
# x = txt2.rjust(12)
# print(x, "is my favorite fruit.")
# 36 rpartition()  Returns a tuple where the string is parted into three parts
# txt = "apple-banana-orange"
#
# x = txt.rpartition("a")
#
# print(x)
# 37 rsplit()  Splits the string at the specified separator, and returns a list
# txt = "apple, banana, cherry"
#
# x = txt.rsplit(", ")
#
# print(x)
# 38    rstrip()  Returns a right trim version of the string
# txt = "     banana     "
#
# x = txt.rstrip()
#
# print("of all fruits", x, "is my favorite")

# 39 rstrip()  Returns a right trim version of the string
# txt = "Apple     "
#
# print(txt.rstrip())
# 44 split()  Splits the string at the specified separator, and returns a list
# txt = "   olma  "
# print(txt.split())
# 45
# txt = "Python"
# print(txt.startswith("P"))  # True
#
# txt = "a\nb\nc"
# print(txt.splitlines())
# 1 append()  Adds an element at the end of the list
# fruits = ["apple", "banana", "cherry"]
#
# fruits.append("orange")

# print(fruits)

# txt = ["olma", 'Anor', "anjir"]
# txt.append("Banan")
# print(txt)

# 2 clear()  Removes all the elements from the list
# fruits = ["olma", "anor", "banan"]
#
# fruits.clear()
#
# print(fruits)

# 3 copy()  Returns a copy of the list

# fruits = ["apple", "banana", "cherry"]
# new_fruits = fruits.copy()
# print(new_fruits)
# print(fruits)

# 4 count()  Returns the number of elements with the specified value
# Fruits = ["olma", "Anjir", "olma", "Banan", "Anjir", "apple"]
# Fruits_count = Fruits.count("apple")
# print(Fruits_count)

# 5 extend() Add the elements of a list (or any iterable), to the end of the current lis
# cars = ["malibu", "Nexia 3", "cobalt"]
# cars.extend(["Gentra"])
# print(cars)

# 6 index()  Returns the index of the first element with the specified value
# fruits = ["olma", "anor", "banan"]
#
# x = fruits.index("anor")
#
# print(x)
#
# index = ["olma", "Anjir", "banan", "apple"]
# xt  = index.index("apple")
# print(xt)
# 7 insert() Adds an element at the specified position
# fruits = ["olma", "anor", "banan"]
#
# fruits.insert(1, "anjir")
#
# print(fruits)
#
# insert = ["olma", "Anjir", "Abrikos"]
# fruits.insert(2, "Banan")
# print(fruits)
# 8 pop()  Removes the element at the specified position'
# fruits = ["olma", "anor", "banan"]
#
# fruits.pop(1)
#
# print(fruits)
#
# pops = ["malina", "Anor", "banana"]
# pops.pop(2)
# print(pops)
# 9 remove()  Removes the item with the specified value
# fruits = ["olma", "anor", "banan"]
#
# fruits.remove("anor")
#
# print(fruits)
#
# numbers = [10, 20, 10, 30]
#
# numbers.remove(10)
#
# print(numbers)
# 10 reverse()  Reverses the order of the list
# fruits = ["olma", "anor", "banan"]
#
# fruits.reverse()
#
# print(fruits)
#
# numbers = [1, 2, 3, 4, 5]
#
# numbers.reverse()
#
# print(numbers)
# sort()  Sorts the list
#
# sorts_number = [1,2,3,4,5,5,6,6,6,7,5,121333,35,734,7]
# sorts_number.sort()
# print(sorts_number)
#
# fruits = ["banan", "olma", "anor"]
#
# fruits.sort()
#
# print(fruits)
