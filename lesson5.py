'''son = float(input("Birinchi sonni kiriting: "))
son1 = float(input("Ikkinchi sonni kiriting: "))
if son == son1 :
    print("Sonlar teng")
elif son > son1 :
    print(f"{son} katta {son1} dan")
else :
    print(f"{son} kichik {son1} dan")'''

'''students = ["Ali","Vali","oysha","Sharif","Bolta","tesha"]
# agar student ism 4 tadan kop bulsa print qilish
#len(student[0])
for student in students:
    ism_uzunligi = 0
    #student Ali # Vali
    for letter in student:
        #letter = A
        ism_uzunligi += 1
        if ism_uzunligi > 4:
            print(student)'''

'''a = input("birinchi son")
b = input("ikkinchi son")
if a > b :
    print(a>b)
else :
    print(a < b)
else :
    print()'''

###################### WHILE loop_________________________________12.12.2025
# 1 dan 5 gacha bulgan sonlarni chiqaradi
'''son = 0
while True:
    son+=1
    if son == 5:
        print(f"{son} 5 ga teng buldi")# printni bu yerda yozsa ham buladi
        break
print(f"{son} 5 ga teng buldi")'''
# 1 dan 5 gacha bulgan sonlarni chiqaradi
'''son = 0
while son < 5:
    son+=1
    print(son)'''

# Number guessing game
'''import random
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
'''son = 1
yigindi = 0
while son < 10:
    yigindi = yigindi + son
    son = son+2
print(f"{yigindi} bu toq sonlar yig'indisi")'''

#contune ---> kodni boshiga qaytaradi
#break ---> siklni tuxtatadi
#pass ---> siklni utkazib yuboradi