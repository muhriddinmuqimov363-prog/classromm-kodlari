'''# Number guessing game
import random
komp_number = random.randint(1,10)
print(komp_number)
imkon_soni = 5
while imkon_soni > 0:
    user_num = int(input("raqam kiriting: "))
    if user_num == komp_number:
        print("Siz yutdingiz")
        break
    else:
        print("keyingi raqam k:, hozircha topa olmadingiz:)")
    imkon_soni+=1'''

# Tub son murakkab son
'''n = int(input("sonni k: "))
tub = True
for num in range(2,int(n**0.5)+1):
    if n % num == 0:
        tub = False
        break
if tub:
    print("tub son")
else:
    print("murakkab son")'''

#kitob amaliy
'''ex = True
while True:
    user = input("yoshingizni kiriting: ")
    if user.lower() == 'exit' or user.lower() == 'quit':
        print("Dastur tuxtatildi!")
        break
    yosh = int(user)
    if yosh < 7:
        print("2000")
    elif yosh > 7:
        print("3000")
    else:
        print("Bepul")'''

'''savol = "nimadir kir"
while True:
    qiymat = input("qiymat kiriting: ")
    if qiymat == 'exit':
        break
    elif float(qiymat) < 0:
        print("Musbat son kiriting!")
    else:
        print(f"{float(qiymat)**0.5}")'''

# sonning raqamlar yigindisini topish
# 747 = 7+4+7 = 18
'''user_son = int(input("son kirit: "))
yigindi = 0
while True:
    if user_son == 0:
        break
    yigindi +=user_son % 10
    user_son = user_son // 10
print(yigindi)'''

# Sonning raqamlar yigindisini topish
'''son = int(input("sonni kiriting: "))
yigindi = 0
while True:
    if son == 0:
        break
    yigindi +=son % 10
    son = son//10
print(yigindi)'''
'''raqam = 0
son = int(input("son kiriting: "))
for n in range(1,son+1):
    raqam = raqam * 10 + n
print(raqam)'''

# n = 5 , n = 7
# 12345 , 1234567
# 543210 , 76543210
'''katta_raqam = 0
n = int(input("sonni k: "))
for num in range(1,n+1):
    #num = 3
    katta_raqam = katta_raqam * 10 + num
print(katta_raqam)'''
katta_raqam = 0
n = int(input("sonni k: "))
for num in range(n+1,0):
    num = 1
    katta_raqam = katta_raqam * 10 - num
print(katta_raqam)



