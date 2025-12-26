'''my_set = {'olim',6,5,11,'Vali'}
my_set = list(my_set)
print(my_set[2])'''
'''takror = {}
ismlar = ['Ali','Ali','Vali','Bali','Salim','Sobir','Sanjar','Abbos','Abror','Botur','Tohir']
for n in ismlar:
    if takror.get(n):
        takror[n]+=1
    else:
        takror[n] = 1
print(takror)'''

'''yozuvchilar = []
adiblar = {
    "G'.G'":["Mening o'. b.","sh. b."],
    "O'tkir H.": ["oq kema","ufq"],
    "Alisher Navoiy":["xamsa"],
    #"A. Q.":"K va K"
}
yozuvchilar.append(adiblar)
for n in adiblar:
    if n in adiblar:
        adiblar[n] = ["oydin kechalar"]
        yozuvchilar.append(n)
    else:
        adiblar["Behbudiy"] = ["Esladim"]
print(adiblar)'''

'''adiblar = {
    "G'.G'":["Mening o'. b.","sh. b."],
    "O'tkir H.": ["oq kema","ufq"],
    "Alisher Navoiy":["xamsa"],
    #"A. Q.":"K va K"
}
adib_nomi = input("Adib nomini kiriting: ")
asar = input("Asar nomini kiriting: ")
if adiblar.get(adib_nomi) :
    adiblar.get(adib_nomi).append(asar)
else:
    adiblar[adib_nomi] = [asar]
print(adiblar)'''

'''olimlar = []
olimlar.append({
    "Gofur Gulom":"Shum bola"
})
olimlar.append({
    "Chingiz Aytmatov":"oq kema"
})
olimlar.append({
    "Gofur Gulom":"Mening o'. b."
})
print(olimlar)'''

'''olimlar = {}
olimlar.update({
    "Gofur Gulom":"Shum bola"
})
olimlar.update({
    "Chingiz Aytmatov":"oq kema"
})
olimlar.update({
    "Gofur Gulom":"Mening o'. b."
})
print(olimlar)'''