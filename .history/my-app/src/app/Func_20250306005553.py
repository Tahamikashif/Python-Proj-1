# print ("hello world")


# def Add (x,y):
#    return x+y
# Add(2,7)  
# print(Add)

# //////////////////// From Python Case /////////////////////
# 1.Camel  case,
# 2. Snake case,
# 3.Pascal case,
# 4.Doubble uderscore case,
# 5.lowercase case,


# ////////////////////// From Python Data Types ///////////////

# 1.number,
# 2.Array = list => [],
# 3.object = dic = {},
# 4.Float,
# 5.Boolean,
# 6.None


# user_name = "Abc"
# kuchNah = 123
# AsiKitasi = '''
# Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
# sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
# Ut enim ad minim veniam, 
# quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
# Excepteur sint occaecat cupidatat non proident, 
# sunt in culpa qui officia deserunt mollit anim id est laborum.






# '''
# print(user_name,kuchNah,AsiKitasi)

# Bicycles_name:list[str] = ['strike','eggs']
# print(Bicycles_name)

# // strip() String ke dono taraf (start aur end) se extra spaces ya specific characters ko hata deta hai.
# text = "   hello world   "
# print(text.strip())

# text = "Hello Dunya"
# print(text.replace("hello world","python"))

# # String ko kisi specific character ya space ke hisab se tod kar list mein convert karta hai.
# text = "hello   world"
# print(text.split())  # Output: ['hello', 'world']

# text = "hello world"
# print(text.count("l"))


# text = "hello world"
# print(text.find("dog"))

# text = "1"
# print(text.startswith("1"))

list = []
import re
name1 = input("Please enter your name")
name2 = input("Please enter your phone number")
name3 = input("Please enter your email")
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
if re.match(name3,pattern):
print("Your email is valid",em)
name2 = int(name2)
print(name1,name2)
list.append(name1)
list.append(name2)
print(list)