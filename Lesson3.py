#tuples 
'''my_tuple=(1,2,3,4)
my_list=list(my_tuple)
print(type(my_list))
my_tuple = tuple(my_list)
print(f"my_tuplening data turi {type(my_tuple)})'''
#looping >> sikl degan manoni bildiradi
#for bu takrorlanuvchi sikl
'''my_stud = ["Ali","Vali","Bali"]
for std in my_stud:
    print(std)
    print(f"Salom {std}")'''
'''sonlar=[5,6,7,8,9,4,3,2,1]
#range
for son in range(1,10):
#for son in sonlar:
    print(f"{son} ning kvadrati {son*son}")'''
'''for son in range(0,10,2):
    print(son)'''
# beshta ism kiritilib list kurinishida chiqarish
'''dostlar=[]
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5):
    dostlar.append(input(f"{n}-ismini kiriting: "))
    print(dostlar)'''
#
# Ixtiyoriy beshta sonning urta arifmetigi
'''yigindi=[]
# yigindi=0
for n in range(5):
     user_input=float(input(f"{n+1} - raqamni kiriting: "))
     #yigindi=yigindi+user_input
     yigindi.append(user_input)
print(f"hozirgi yigindi: {yigindi}")
#print(f"ortacha qiymat: {yigindi//5}")
print(f"ortacha qiymat: {sum(yigindi)//5}")'''


'''kopaytma=1
a=int(input("raqm k: "))
for n in range(a):
    data_in = float(input(f"{n+1} - raqamni kiriting: "))
    kopaytma=kopaytma*data_in
print(f"o'rtacha qiymat: {kopaytma//a}")'''

# if else mavzusi
# if else elif
#n=7
#n=-1
'''n=0
if n>0:
    print("n noldan katta")
elif n<0:
    print("n noldan kichik")
else:
    print("n nolga teng")'''
# Taqqoslash operatorlari <,>,>=,<=
'''yosh=int(input(f"yoshingizni kiriting: "))
if yosh < 7 :
    print(f"Sizga kirish bepul")
elif 7<yosh<18:
    print(f"Sizga chipta narxi 1000 som")
elif 18<yosh<55:
    print(f"Sizga chipta narxi 2000 som")'''
#else yosh>55
#print(f"Sizga chiptalar arzon narxda")
'''list=[]
for n in range(10):
    if n%3==0:
        list.append(n)
print(f"{list}")'''
'''a=int(input(f"1 dan 100 gacha ixtiyoriy son kiriting: "))
for n in range(a):
    if n%15==0:
        print("FizzBuzz")
    elif n%5==0:
        print("Buzz")
    elif n%3==0:
        print("Fizz")'''
'''son=[]
raqam=[]
a=int(input(f"1 dan 100 gacha ixtiyoriy son kiriting: "))
for n in range(a):
    if n%10==0:
        son.append(n%10==0)
        print(son)
    elif n%5==0 and n%3==0:
        raqam.append(n%5==0)
        print(raqam)
    elif n%3==0:
        raqam.append(n%3==0)
        print(raqam)'''
