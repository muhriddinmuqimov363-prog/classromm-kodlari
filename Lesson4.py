#Foydalanuvchi n ta float son kiritsin hammasi 2ga kopaytirilib chiqsin
'''n = int(input("nechta son kiritasiz: "))
for son in range(1,n+1):'''
'''baholar=[]
n = int(input("7 ta son kiritasiz: "))
for n in range(7):
    raqam=float(input(f"{n}-bahoni kiriting: "))
    baholar.append(raqam)
    baholar_sum=sum(baholar)
    baholar_s=baholar_sum/n
    if baholar_s<60:
        print("fail")
    elif baholar_s>86:
        print("Alo")
    elif baholar_s>71 and baholar_s<86:
        print("yaxshi")
    elif baholar_s>65 and baholar_s<71:
        print("o'rtacha")'''

#sonlar = float(input("istalgan son kiriting: "))
'''sonlar = list(range(20))
for son in sonlar:
    print(f"{son} ning ko'paytmasi {son*2} ga teng")'''
'''n=int(input("son kiriting: "))
for i in range(1):
    print(n*2)'''
'''unlilar = "aeuio"
a=[]
b=[]
#unlilar = int(unlilar)
name = "Muhriddin Muqumov".lower()
for char in name:
    if char in unlilar:
        print(f"{char} unli harf")
        a.append(char)
        #print(f"{a} unlilar soni")
    else:
        print(f"{char} undosh harflar")
        b.append(char)
        #print(f"{b} undoshlar soni")
print(f"{len(a)} ta - unli harflar soni")
print(f"{len(b)} ta - undosh harflar soni")'''