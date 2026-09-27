from os import getenv
import asyncio
from aiogram import Bot, Dispatcher, Router
from dotenv import load_dotenv
from handlers.routes import router, notifaer
load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()

dp.include_router(router)



async def main():
    bot = Bot(token=TOKEN)

    asyncio.create_task(notifaer(bot))

    print("Hello")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())





























# import json
# user = {
#     "name": "danea",
#     "age": 12,
#     "cty": "fafa"
# }
# with open("user.json", "w", encoding="utf_8") as file:
#     json.dump(user, file)





# numb = 0
# firstnumb = 0
# operation = ""
# result1 = False
# def add_num(num):
#     global numb
#     global result1
#     if result1 == True:
#         numb = 0
#         result1 = False
#     numb = numb * 10 + num
#     if operation == "":
#         labe.config(text=numb)
#     else:
#         labe2.config(text=numb)
#
# def clear():
#     global numb
#     numb = 0
#     global operation
#     operation = ""
#     global result1
#     result1 = False
#     labe.config(text="-")
#     labe1.config(text="?")
#     labe2.config(text="-")
#     labe3.config(text="-")
#
# def oper(op):
#     global numb
#     global operation
#     global firstnumb
#     firstnumb = numb
#     numb = 0
#     operation = op
#     if op == "+":
#         labe1.config(text="+")
#     elif op == "-":
#         labe1.config(text="-")
#     elif op == "*":
#         labe1.config(text="*")
#     else:
#         labe1.config(text="/")
#
# def rovno():
#     global numb
#     global result1
#     global operation
#     if operation == "+":
#         numb = firstnumb + numb
#     elif operation == "-":
#         numb = firstnumb - numb
#     elif operation == "*":
#         numb = firstnumb * numb
#     elif operation == "/":
#         if numb != 0:
#             numb = firstnumb / numb
#         else:
#             labe3.config(text="nezea")
#             return
#     result1 = True
#     operation = ""
#     labe3.config(text=numb)
#
# window = tk.Tk()
# window.title("my prgramm")
# window.geometry("500x400")
# button1 = tk.Button(window, text="1", command=lambda: add_num(1))
# button1.grid(row=0, column=0)
# button2 = tk.Button(window, text="2", command=lambda: add_num(2))
# button2.grid(row=0, column=1)
# button3 = tk.Button(window, text="3", command=lambda: add_num(3))
# button3.grid(row=0, column=2)
# button1 = tk.Button(window, text="4", command=lambda: add_num(4))
# button1.grid(row=1, column=0)
# button2 = tk.Button(window, text="5", command=lambda: add_num(5))
# button2.grid(row=1, column=1)
# button3 = tk.Button(window, text="6", command=lambda: add_num(6))
# button3.grid(row=1, column=2)
# button1 = tk.Button(window, text="7", command=lambda: add_num(7))
# button1.grid(row=2, column=0)
# button2 = tk.Button(window, text="8", command=lambda: add_num(8))
# button2.grid(row=2, column=1)
# button3 = tk.Button(window, text="9", command=lambda: add_num(9))
# button3.grid(row=2, column=2)
# button3 = tk.Button(window, text="0", command=lambda: add_num(0))
# button3.grid(row=3, column=1)
# button4 = tk.Button(window, text="C", command=clear)
# button4.grid(row=3, column=0)
# button5 = tk.Button(window, text="+", command=lambda: oper("+"))
# button5.grid(row=0, column=3)
# button7 = tk.Button(window, text="-", command=lambda: oper("-"))
# button7.grid(row=1, column=3)
# button7 = tk.Button(window, text="*", command=lambda: oper("*"))
# button7.grid(row=2, column=3)
# button7 = tk.Button(window, text="/", command=lambda: oper("/"))
# button7.grid(row=3, column=3)
# button6 = tk.Button(window, text="=", command=rovno)
# button6.grid(row=3, column=2)
# labe = tk.Label(window, text="-")
# labe.grid(row=0, column=4)
# labe1 = tk.Label(window, text="-")
# labe1.grid(row=1, column=4)
# labe2 = tk.Label(window, text="-")
# labe2.grid(row=2, column=4)
# labe3 = tk.Label(window, text="-")
# labe3.grid(row=3, column=4)
# # text_box = tk.Text(window)
# # text_box.pack()
# window.mainloop()

# num1 = int(input("Vvedite 1 chislo: "))
# num2 = int(input("Vvedite 2 chislo: "))
# opera = input("Vvediite operatiiu: ")
# if opera == "+":
#     print(num1 + num2)
# elif opera == "-":
#     print(num1 - num2)
# elif opera == "/":
#     print(num1 * num2)
# elif opera == "/":
#     if num2 != 0:
#         print(num1 / num2)
#     else:
#         print("Nelzia")





# labe = tk.Label(window, text="hui")
# labe.pack()
# entry = tk.Entry(window)
# entry.pack()

# path = filedialog.askopenfilename()
#     with open(path, "w", encoding="utf_8") as file:
#
#         txt = text_box.get("1.0", tk.END)
#         file.write(txt)

# speed(7)
# tracer(2)
# bgcolor('black')
# for i in range(360):
#     color('blue')
#     circle(360 - i, 90)
#     left(90)
#     circle(360 - i, 80)
#     left(16)
# done()










# with open("dada/text.txt", 'r', encoding='utf_8') as file:
#     txt = file.read()
#     txt = txt.strip().lower().replace("полина", "данечка").replace("полину", "данечку").replace("она", "он")
# with open("dada/text.txt", 'w', encoding="utf_8") as file:
#     txt = file.write(txt)
# with open("dada/text.txt", 'r', encoding='utf_8') as file:
#     txt = file.read()
#     print(txt)







# txt = "I love your beautiful mummy"
# cl = txt.split()
# longest = ""
# for i in cl:
#       if len(i) > len(longest):
#           longest = i
# print(longest,'\n', "Dlina =", len(longest))









# with open("dada/text.txt", "r", encoding="utf_8") as file:
#     lines = file.readlines()
#     rezult = []
#     for i in lines:
#         i = i.strip()
#         rezult.append(i.capitalize())
# with open("dada/text.txt", "w", encoding="utf_8") as file:
#     users = file.write("\n".join(rezult))
# with open("dada/text.txt", "r", encoding="utf_8") as file:
#     text = file.read()
#     print(text)






# for index, i in enumerate(lines, start=1):
#     print(index, i.strip())







# file = open("dada/text.txt", "r")
# text = file.read()
# print(text)
# file.close()
#




# use = [
#     {"name": "Alex", "age": 17},
#     {"name": "Gob", "age": 22},
#     {"name": "Charlie", "age": 19},
#     {"name": "David", "age": 16}
# ]
#
# nums = [1, 3, 4, 1, 3, 2, 3,]
# res = {}
# for num in nums:
#     res[num] = res.get(num, 0) + 1
# print(res)

# result = [user["name"] for user in users]
# sort = list(set(result))
# print(sort)

# numbers = [1, 4, 1, 5, 5, 7, 1, 7]
# rezult = list(set(numbers))
# print(rezult)
# names = ["Alex", "Bob", "Alex", "Charle"]
# res = list(set(names))
# print(res)

# uesr = {
#     "name" : "Alex",
#     "age" : 12
# }
# print(uesr.get("name"))
# print(uesr.get("email", "E-mail Nety!"))




# while True:
#     try:
#         your_age = int(input("Введите число: "))
#         if 1 < your_age < 120:
#             print("rhodite")
#             break
#         else:
#             print("Ti ebanat? ")
#     except ValueError:
#         print("ne")





# res = [user["name"].upper() for user in users if user["age"] > 18]
# print(res)

# result = [user for user in users if user["age"] > 18]
# print(result)




# class pidor:
#     name = None
#     age = None
#     isHappy = None
#
#     def __init__(self, name, age, isHappy):
#         self.set_data(name, age, isHappy)
#
#         self.get_data()
#
#     def set_data(self, name, age, isHappy):
#         self.name = name
#         self.age = age
#         self.isHappy = isHappy
#
#     def get_data(self):
#         print(self.name, "age",self.age, "Happy:", self.isHappy )
#
# fedea = pidor("pisiun", 13, False)
#
# sanea = pidor("ebanat", 11, True)



# time.sleep(1) #модуль sleep замораживает работу программы на указанное в скобка время
# print("ia pidor")





# try:
#     with open('dada/text.txt', 'r', encoding="utf-8" ) as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File is not funded")



# file = open('dada/text.txt', 'r')
#
# #print(file.read())
#
# for lne in file:
#     print(lne)
#
# file.close()


# data = input("Введите текст: ")
# file = open('dada/text.txt', 'w')
#
# file.write(data)
#
# file.close()


# users = [
#     {"name": "Alex", "age": 17},
#     {"name": "Gob", "age": 22},
#     {"name": "Charlie", "age": 19},
#     {"name": "David", "age": 16}
# ]
# age1 = int(input("esti li v chate hot iodin polizovateli starshe: "))
# def find(users, age1):
#     return any(user["age"] > age1 for user in users)
#
#
# print(find(users, age1))


# result.append(user)
#
#     return result

# users = [
#     {"name": "  aLeX", "city": "CHISINAU"},
#     {"name": "BOB  ", "city": "balti"},
#     {"name": "  Charlie  ", "city": "CHISINAU"},
#     {"name": "DAVID", "city": "cahul"}
# ]
# def newpaper(users):
#     cleanest = []
#     n_user = users.copy()
#     for user in n_user:
#         user["name"] = user["name"].strip()
#         user["name"] = user["name"].capitalize()
#         user["city"] = user["city"].lower()
#         cleanest.append(user)
#     return cleanest
#
#
# print(newpaper(users))


# def stats(users):
#     status = {}
#     long = len(users)
#     status["count"] = long
#     oldest = max(users, key=lambda user: user["age"])
#     status["oldest"] = oldest["name"]
#     young = min(users, key=lambda user: user["age"])
#     status["young"] = young["name"]
#     return status
#
#
# print(stats(users))


# resukt = max(users, key=lambda user: user["age"])
# young = min(users, key=lambda user: user["age"])
# print(resukt["name"], young["name"])






# shema = input("Числа или геометрия? ")
# if shema == '1':
#
#     a = int(input("1 = "))
#     b = int(input("2 = "))
#     op = input("eperatin = ")
#
#     def chisla(a, b, op):
#
#         if op == '+':
#             c = a + b
#         elif op == '-':
#             c = a - b
#         elif op == '*':
#             c = a * b
#         elif op == '/':
#             c = a / b
#         return c
#     print(chisla(a, b, op))
# elif shema == '2':
#     Razdel = input("Для раздела площади выберите 1 " "Для периметра выберите 2 ")
#     if Razdel == '1':
#         figura = input("Напишите навание фигуры ")
#         if figura == 'треугольник':
#             print("Введите основание и высоту ")
#             osnovanie = int(input())
#             vista = int(input())
#             P = (1/2 * osnovanie) * vista
#             print(P)















# users = [
#     {"name": "  alex", "age": 17},
#     {"name": "BOB  ", "age": 22},
#     {"name": "  charlie  ", "age": 19},
#     {"name": "DAVID", "age": 16}
# ]
#
# def vzroslii(users):
#     approved = []
#     for user in users:
#         if user["age"] > 18:
#             approved.append(user)
#     return approved
#
# result = vzroslii(users)
#
# def clean(result):
#     cleaner = []
#     for user in result:
#         user["name"] = user["name"].strip()
#         user["name"] = user["name"].capitalize()
#         cleaner.append(user)
#     return cleaner
# print(clean(result))





# names = ["  alex", "BOB  ", "  Charlie  ", "david"]
# def nas(names):
#     fd = []
#     for i in names:
#         i = i.strip()
#         i = i.capitalize()
#         fd.append(i)
#
#
#
#     return fd
# print(nas(names))







# products = {
#     "apple": 2,
#     "banana": 1,
#     "milk": 3,
#     "bread": 4
# }
# def pr(products):
#     rt = {}
#     for name, price in products.items():
#         if price > 2:
#             rt[name] = price
#     return rt
# print(pr(products))
#






# num = [7, 23, 4, 91, 18, 42 ]
# def kv(num):
#     kr = []
#     for i in num:
#         kr.append(i * i)
#     return kr
# print(kv(num))




# biggest = []
# def big(num):
#     for i in num:
#
#         if i > 20:
#             biggest.append(i)
#     return biggest
# print(big(num))




# def klo(num):
#     result = []
#     for n in num:
#         p = n * n
#         result.append(p)
#     return result
# print(klo(num))




# num = [7, 23, 4, 91, 18, 42 ]
# def maxi(num):
#     big = 0
#     s = 0
#     i = 0
#     for n in num:
#         s = s + n
#         if n % 2 == 0:
#             i += 1
#         if n > big:
#             big = n
#     return s, i, big
# print(maxi(num))

# num = [7, 23, 4, 91, 18, 42 ]
# def max(num):
#     s = 0
#     for n in num:
#         if n % 2 == 0:
#             s = s + n
#     return s
# print(max(num))




# num = [4,15,2,30,8,21]
# def cul(num):
#     i = 0
#     for n in num:
#         if n > 10:
#             i = i + 1
#     return i
# print(cul(num))








# num = [12, 5, 8,21,4,16,9]
# s = 0
# def sum(num, s):
#      for n in num:
#         s = s + n
#      return s
#
# print(sum(num, s))





# a = int(input("1 = "))
# b = int(input("2 = "))
# op = input("Oper = ")
# def calc(a, b, op):
#     if op == '+':
#         return a + b
#     elif op == '-':
#         return a - b
#     elif op == '*':
#         return a * b
#     elif op == "/" and b != 0:
#         return a / b
# print(calc(a, b, op))





# a = int(input("a = "))
# def sq():
#     return a * a
# b = sq()
# print(b)





# s = 0
# nes = 0
# num = [5, 12, 7, 20, 3, 19 ]
# for n in num:
#     if n % 2 == 0:
#         s = s + 1
#     else:
#         nes = nes + 1
#
# print(s, nes)







# for i in range(10, 0, -1):
#     print(i)







# n = random.randint(1, 100)
# c = int(input("Chislo "))
# i = int(1)
# while n != c:
#     if n > c:
#         print("Bolishe!")
#     elif n < c:
#         print("Menishe!")
#     c = int(input("Chislo " ))
#     i = i + 1
# if n == c:
#     print("verno! u tebea uslo", i, "popitok")






# while True:
#     try:
#         a =int(input("VVedi 1 chislo: "))
#         b =int(input("VVedi 2 chislo: "))
#         break
#     except ValueError:
#         print("Vvedi pravilno!")
#
# op = input("VVedi operaciu: ")
#
# if op == "+":
#     c = a + b
#     print(c)
# elif op == "-":
#     c = a - b
#     print(c)
# elif op == "*":
#     c = a * b
#     print(c)
# elif op == "/":
#     if b != 0:
#         c = a / b
#         print(c)
#     elif b == 0:
#         print("error")
#         exit()
# else:
#     print("Prosti ia takoe ne znaiu(")
#
# i = input("Hochesi povtoriti? (+ / -): ")
# while i == '+':
#     a = int(input("VVedi 1 chislo: "))
#     b = int(input("VVedi 2 chislo: "))
#     op = input("VVedi operaciu: ")
#     if op == "+":
#         c = a + b
#         print(c)
#     elif op == "-":
#         c = a - b
#         print(c)
#     elif op == "*":
#         c = a * b
#         print(c)
#     elif op == "/":
#         if b != 0:
#             c = a / b
#             print(c)
#         else:
#             print("error")
#     else:
#         print("Prosti ia takoe ne znaiu(")
#
#     i = input("Povtorim? (+ / -) ")
# if i == '-':
#     print("ok")


