# # 1. Susikurkite tuple iš studijų programos modulių pavadinimų.
# # Atspausdinkite šiuos pavadinimus sąraše, prieš kiekvieną pavadinimą
# # išvedant brūkšniuką. Raskite ilgiausią modulio pavadinimą.
#
# # Ka padaryti?
#
# tuple = ('tuples', 'dictionaries', 'sets')
# for x in tuple:
#     print(f'-{x}')
#
# print(max(map(len,tuple)))
#
# longest_name = max(tuple, key=len)
# print(longest_name)
#
# # Susikurkite tuple iš mėnesių pavadinimų. Susikurkite kitus tuples
# # sezonams apibūdinti: žiema, pavasaris, vasara, ruduo. Panaudokite slicing
# # [start:end], kad atitinkamus mėnesius sudėtumėte į atitinkamus sezonų
# # tuples. Šį priskyrimą turite atlikti kuriant individualius sezonų tuples, kitaip
# # išmes klaidą, kad jo negalite modifikuoti.
#
# menesiai = ('sausis', 'vasaris', 'kovas',
# 'balandis', 'geguze', 'birzelis', 'liepa',
# 'rugpjutis', 'rugsejis', 'spalis', 'lapkritis',
# 'gruodis')
#
# print(f'Spring: {menesiai[2:5]}')
# print(f'Summer: {menesiai[5:8]}')
# print(f'Autumn: {menesiai[8:11]}')
# print(f'Winter: {menesiai[11:12] + menesiai[0:2]}')
#
# 1

# studentas = {
#     'vardas': 'Tomas',
#     'Pavarde': 'Staniulis',
#     'amzius': 19,
#     'Studiju programa': 'Suvirontojas',
#     'Kredytu skaicius': 10,
#     'pazymiai': [8, 7, 9, 10],
#     'Ugis': 1.87,
#     'Kursas': 1,
#     'Istaiga': 'Viko'
# }
#
# print(studentas)
#
# print(studentas['vardas'])
# print(studentas['Ugis'])
# print(studentas['Istaiga'])
#
# 2

import datetime
from traceback import print_tb

#
# filmas = {
#     'Pavadinimas': 'The Substance',
#     'Rezisierius': 'Coralie Fargeat',
#     'Biudzetas': ['$', 17.5, 'million'],
#     'Uzdarbys': ['$', 39.1, 'million'],
#     'Zanras': 'body horror',
#     'Ilgis': '141 minutes',
#     'Isleidimo metai': [20, 'September', 2024],
#     'Aktoriu sarasas': ['Demi Mūr', 'Margaret Qualley', 'Denis Kveidas', 'Hugo Diego Garcia']
# }
#
# print(filmas)
# pelnas = filmas['Uzdarbys'][1] - filmas['Biudzetas'][1]
# print(pelnas)
#
# count = 0
#
# for x in filmas['Aktoriu sarasas']:
#     count += 1
#
# print(f'Aktoriu kiekis: {count}')
#
# print(f'Metu filmui: {filmas['Isleidimo metai'][2] - datetime.date.today().year}')

# 3

# knyga1 = {
#     "pavadinimas": "Vėjų medžiotojai",
#     "autorius": "Jonas Pavardė",
#     "žanras": "Nuotykinė literatūra",
#     "kaina": 15.99,
#     "puslapių kiekis": 320,
#     "skyriai": ["Pradžia", "Kelionės pradžia", "Audros", "Nuotykiai jūroje", "Atrastos paslaptys", "Pabaiga"],
#     "išleidimo metai": 2021,
#     "galima rasti knygynuose": True
# }
#
# knyga2 = {
#     "pavadinimas": "Laiko šešėliai",
#     "autorius": "Viktorija Raštaitė",
#     "žanras": "Fantastika",
#     "kaina": 19.49,
#     "puslapių kiekis": 420,
#     "skyriai": ["Laiko įvadas", "Magiškos būtybės", "Tamsos užtemimas", "Drąsos išbandymas", "Galutinė kova", "Atgimimas"],
#     "išleidimo metai": 2018,
#     "galima rasti knygynuose": False
# }
#
# print(knyga1)
# print(knyga2)
#
# if knyga2['puslapių kiekis'] > knyga1['puslapių kiekis']:
#     print('Pirma knyga plonesne')
# elif knyga2['puslapių kiekis'] < knyga1['puslapių kiekis']:
#     print('Antra knyga plonesne')
# else:
#     print('Pusplaiu skaicius vienodas')
#
# count1 = 0
# count2 = 0
#
# for x in knyga1['skyriai']:
#     count1 += 1
#
# for u in knyga2['skyriai']:
#     count2 += 1
#
# if count1 > count2:
#     print('Pirma knyga turi daugiau skyriu')
# if count1 < count2:
#     print('Antra knyga turi daugiau skyriu')
# else:
#     print('Lygus skyriu skaicius')
#
# if knyga1['kaina'] > knyga2['kaina']:
#     print('Knyga pirma yra brangesne')
#     dviguba = knyga2['kaina'] * 2
#     if dviguba > knyga1['kaina']:
#         print('Padvigubinta suma antros knygos, butu brangesne uz pirmos knygos kaina')
# if knyga1['kaina'] < knyga2['kaina']:
#     print('Knyga antra yra brangesne')
#     dviguba = knyga1['kaina'] * 2
#     if dviguba > knyga2['kaina']:
#         print('Padvigubinta suma pirmos knygos, butu brangesne uz antros knygos kaina')

# 4

# preke1 = {
#     "pavadinimas": "Kavos aparatas",
#     "kaina": 150.00,
#     "savikaina": 90.00,
#     "kodas": "KA12345",
#     "kiekis_sandelyje": 25,
#     "dezes_matmenys": {"x": 30, "y": 25, "z": 35}
# }
#
# preke2 = {
#     "pavadinimas": "Bevielės ausinės",
#     "kaina": 50.00,
#     "savikaina": 20.00,
#     "kodas": "BA56789",
#     "kiekis_sandelyje": 100,
#     "dezes_matmenys": {"x": 10, "y": 8, "z": 5}
# }
#
# preke3 = {
#     "pavadinimas": "Nešiojamas kompiuteris",
#     "kaina": 800.00,
#     "savikaina": 500.00,
#     "kodas": "NK34567",
#     "kiekis_sandelyje": 15,
#     "dezes_matmenys": {"x": 40, "y": 30, "z": 5}
# }
#
# print(preke1)
# print(preke2)
# print(preke3)
# print(f'Pirma preke kainuoja: {preke1['kaina']} Eur, Antra preke kainuoja: {preke2['kaina']} Eur, Trecia preke kainuoja: {preke3['kaina']} Eur')
#
# if preke1['kaina'] > preke2['kaina'] and preke1['kaina'] > preke3['kaina']:
#     print(f'Brangiausia preke pirma: {preke1}')
# if preke1['kaina'] > preke3['kaina'] and preke1['kaina'] > preke2['kaina']:
#     print(f'Brangiausia preke pirma: {preke1}')
# if preke2['kaina'] > preke3['kaina']:
#     print(f'Brangiausia preke antra: {preke2}')
# if preke3['kaina'] > preke2['kaina']:
#     print(f'Brangiausia preke trecia: {preke3}')
#
# print(f'Pirmos dezes turis: {preke1['dezes_matmenys']['x'] * preke1['dezes_matmenys']['y'] * preke1['dezes_matmenys']['z']}')
# print(f'Antros dezes turis: {preke2['dezes_matmenys']['x'] * preke2['dezes_matmenys']['y'] * preke2['dezes_matmenys']['z']}')
# print(f'Trecios dezes turis: {preke3['dezes_matmenys']['x'] * preke3['dezes_matmenys']['y'] * preke3['dezes_matmenys']['z']}')
#
# print(f'Pelningumas: {(preke1['kaina'] - preke1['savikaina']) * preke1['kiekis_sandelyje']}')
# print(f'Pelningumas: {(preke2['kaina'] - preke2['savikaina']) * preke2['kiekis_sandelyje']}')
# print(f'Pelningumas: {(preke3['kaina'] - preke3['savikaina']) * preke3['kiekis_sandelyje']}')

# 5

# automobilis = {}
#
# automobilis["marke"] = "Toyota"
# automobilis["modelis"] = "Supra mk4"
# automobilis["rida"] = 85600
# automobilis["gamybos_metai"] = 1993
# automobilis["spalva"] = "juoda"
# automobilis["darbinis_turis"] = 3.0
# automobilis["ar_dauzta"] = False
# automobilis["ar_parduodama"] = True
#
# print(automobilis)
#
# metu = datetime.date.today().year - automobilis['gamybos_metai']
# print(f"Metų skaičius nuo pagaminimo: {metu}")
#
# print(f'Vidutiniskai masina nuvaziavo per metus: {automobilis["rida"] / metu} kilometru')

# 6
#
# automobilis = {}
#
# automobilis["marke"] = "Toyota"
# automobilis["modelis"] = "Supra mk4"
# automobilis["rida"] = 85600
# automobilis["gamybos_metai"] = 1993
# automobilis["spalva"] = "juoda"
# automobilis["darbinis_turis"] = 3.0
# automobilis["ar_dauzta"] = False
# automobilis["ar_parduodama"] = True
#
# print(f' It\'s crazy {automobilis['marke'], automobilis['modelis']}')

# 7
#
# bookstore_info = {
#     "pavadinimas": "Knygų pasaulis",
#     "adresass": "Vilniaus g. 10, Vilnius",
#     "plotas_kv_m": 120,
#     "kiek_knygų": 3000,
#     "darbo_valandos": {
#         "pirmadienis": "10:00 - 18:00",
#         "antradienis": "10:00 - 18:00",
#         "trečiadienis": "10:00 - 18:00",
#         "ketvirtadienis": "10:00 - 18:00",
#         "penktadienis": "10:00 - 20:00",
#         "šeštadienis": "10:00 - 18:00",
#         "sekmadienis": "uždaryta"
#     },
#     "ar_atidarytas": True
# }
#
# for key in bookstore_info:
#     print(key, ':', bookstore_info[key])

# Išveskite šio knygyno
# dictionary raktus su reikšmėmis.

# 8

# Raskite abiejų studentų pažymių
# vidurkius. Išveskite abiejų studentų informaciją, bei pažymių vidurkius.
# Raskite ir išveskite, kurio studento pažymių vidurkis yra didesnis ir
# išveskite jo vardą su pavarde.

# student1 = {
#     "vardas": "Jonas",
#     "pavardė": "Jonaitis",
#     "studijų_programa": "Informatika",
#     "pažymiai": [4, 7, 9, 8 , 10, 4]
# }
#
# student2 = {
#     "vardas": "Aistė",
#     "pavardė": "Paliulytė",
#     "studijų_programa": "Verslo vadyba",
#     "pažymiai": [9, 8, 7, 10, 5, 6]
# }
# count1 = 0
# count2 = 0
#
# for grade in student1['pažymiai']:
#     count1 += grade
#
# for grade in student2['pažymiai']:
#     count2 += grade
#
# # print(f'Pirmo vidurkis: {count1 / len(student1['pažymiai'])}')
# # print(f'Pirmo vidurkis: {count2 / len(student2['pažymiai'])}')
#
# student1['vidurkis'] = count1 / len(student1['pažymiai'])
# student2['vidurkis'] = count2 / len(student2['pažymiai'])
#
# print(student1)
# print(student2)
#
# if student1['vidurkis'] > student2['vidurkis']:
#     print(f'{student1['vardas'], student1['pavardė']} vidurkis didesnis')
# if student1['vidurkis'] < student2['vidurkis']:
#     print(f'{student2['vardas'], student2['pavardė']} vidurkis didesnis')

# 9

# Susikurkite dictionary, kuriame būtų nurodytos prekės ir turimi kiekiai, t.y.
# raktas yra prekės pavadinimas ir reikšmė yra turimas prekės kiekis, o visa
# tai saugoma viename dictionary (panašu į 29 pavyzdį). Išveskite visą
# turimą dictionary informaciją gražiai suformatuotai, pvz: '- Prekės
# "Pieštukas" liko 132 vnt.' ir tai padaryti atskirose eilutėse.
# Taip pat, raskite
# ir išveskite visų prekių bendrą turimą kiekį (sudėti visus turimus kiekius),
# kiekių vidurkį (kiek vidutiniškai turima prekių). O tos prekės kurios likę
# mažiausiai vienetų išvesti pavadinimą ir kiekį.

# dictionary = {
#     'mangos': 34,
#     'bananas': 54,
#     'apples': 20,
#     'oranges': 54,
#     'grapes': 228,
#     'coconuts':12
# }
#
# for i, x in dictionary.items():
#     print(f'{i} product, we have {x} units' )
#
# sum = 0
# count = 0
# for item, amount in dictionary.items():
#     sum += amount
#     count += 1
#
# print(f'Is viso yra: {sum}')
# print(f'Vidurkis prekiu: {sum / count}')
#
# print(min(dictionary, key=dictionary.get)) #SURANDA MAZIAUSIA REIKSME

# 10

# 10.Susikurkite dictionary darbuotojo informacijai saugoti. Nurodykite tokias
# savybes: vardas ir pavardė, telefonas, profesija, etatas, atlyginimas. Taip
# pat, sukurkite dar vieną darbuotojo dictionary, tačiau nenurodykite 1-os
# ar 2-ų savybių, pvz, praleiskite profesiją.
# Parašykite tokią programą, kuri
# galėtų išsiaiškinti kurios(-ių) savybių nėra antrame dictionary, kurios yra
# pirmame, pvz jeigu nėra profesijos, tai programa išsiaiškintų, kad nėra
# nurodyta profesija antrame dictionary. Padarykite taip, kad vartotojas
# turėtų galimybę suvesti trūkstamas savybes.

# dar1 = {
#     "vardas": "Tomas",
#     "pavardė": "Petraitis",
#     "telefonas": "+370 612 34567",
#     "profesija": "Programuotojas",
#     "etatas": "Pilna darbo diena",
#     "atlyginimas": 2500
# }
#
# dar2 = {
#     "vardas": "Laura",
#     "pavardė": "Zablockytė",
#     "telefonas": "+370 698 76543",
#     "etatas": "Pusė darbo dienos",
#     "atlyginimas": 1200
# }
#
# for key in dar1:
#     if key in dar2:
#         continue
#     else:
#         print(f'Nera sios reiksmes, antram dictionary: {key}')
#         if key == dar1['atlyginimas']:
#             print(f'Papildykite {key}')
#             reiksme = input(int('Jusu skaicus: '))
#             dar2[key] = reiksme
#         else:
#             print(f'Papildykite {key}')
#             reiksme = input('Jusu duomenys: ')
#             dar2[key] = reiksme
#
# for key in dar2:
#     if key in dar1:
#         continue
#     else:
#         print(f'Nera sios reiksmes, antram dictionary: {key}')
#         if key == dar2['atlyginimas']:
#             print(f'Papildykite {key}')
#             reiksme = input(int('Jusu skaicus: '))
#             dar1[key] = reiksme
#         else:
#             print(f'Papildykite {key}')
#             reiksme = input('Jusu duomenys: ')
#             dar1[key] = reiksme
#
# print(dar1)
# print(dar2)

# 11

# 11.Kaimynystėje yra trys kepyklos, apie kiekvieną yra žinoma ši informacija:
# pavadinimas; darbuotojų kiekis; adresas; praeitos savaitės iškeptų kepinių
# kiekiai (sąrašas su 7-iais elementais, kur nurodyti atskiri kepinių kiekiai).
# Susikurkite dictionaries kiekvienai kepyklai.
# Jeigu vienas kepinys
# parduodamas už 1.5 euro, raskite kuri kepykla galėjo būti pelningiausia.
# Taip pat, išsiaiškinkite kiek vidutiniškai kiekviena kepykla per dieną
# pagamina kepinių, raskite kurios kepyklos vidurkis mažiausias.

# kepykla1 = {
#     "darbuotojų kiekis": 10,
#     "adresas": "Gedimino pr. 1, Vilnius",
#     "kiekiai per savaite": {'Spurgos': 10,
#                 'Sumustiniai': 20,
#                 'Kruasanas': 30,
#                 'Bandeles su aguonomis': 10,
#                 'Bandele su persikais': 15,
#                 'Bandele su sokoladu': 25,
#                 'Sausainiai': 35
#                 }
# }
#
# kepykla2 = {
#     "darbuotojų kiekis": 15,
#     "adresas": "Laisvės al. 10, Kaunas",
#     "kiekiai per savaite": {'Spurgos': 30,
#                 'Sumustiniai': 10,
#                 'Kruasanas': 35,
#                 'Bandeles su aguonomis': 25,
#                 'Bandele su persikais': 15,
#                 'Bandele su sokoladu': 55,
#                 'Sausainiai': 25
#                 }
# }
#
# kepykla3 = {
#     "darbuotojų kiekis": 20,
#     "adresas": "Taikos pr. 50, Klaipėda",
#     "kiekiai per savaite": {'Spurgos': 50,
#                 'Sumustiniai': 30,
#                 'Kruasanas': 40,
#                 'Bandeles su aguonomis': 55,
#                 'Bandele su persikais': 25,
#                 'Bandele su sokoladu': 50,
#                 'Sausainiai': 35
#                 }
# }
#
#
# k1 = sum(kepykla1["kiekiai per savaite"].values())
# k2 = sum(kepykla2["kiekiai per savaite"].values())
# k3 = sum(kepykla3["kiekiai per savaite"].values())
#
# if k1 * 1.5 > k2 * 1.5 > k3 * 1.5:
#     print(f'Pirma kepykla wins: {k1*1.5} kiekiu')
# if k1 * 1.5 > k3 * 1.5 > k2 * 1.5:
#     print(f'Pirma kepykla wins: {k2*1.5} kiekiu')
# if k3 * 1.5 > k2 * 1.5:
#     print(f'Trecia kepykla wins: {k3*1.5} kiekiu')
# else:
#     print(f'Antra kepykla wins: {k2*1.5} kiekiu')
#
# print(f'Pirmos kepyklos vidurkis, pagamintu bandeliu per diena: {k1 / 5}')
# print(f'Pirmos kepyklos vidurkis, pagamintu bandeliu per diena: {k2 / 5}')
# print(f'Pirmos kepyklos vidurkis, pagamintu bandeliu per diena: {k3 / 5}')
#
# v1 = k1 / 5
# v2 = k2 / 5
# v3 = k3 / 5
#
# if v1 < v2 and v1 < v3:
#     print(f'Pirma maziausiai: {v1}')
# elif v2 < v3 and v2 < v1:
#     print(f'Antra maziausiai: {v2}')
# elif v3 < v2 and v3 < v1:
#     print(f'Trecia maziausiai: {v3}')

# 12

# 12.Susikurkite sąrašą, kuriame būtų saugomos skirtingos knygos (kaip
# dictionary elementai). Apie kiekvieną knygą į atskirus knygų dictionary
# sudėkite norimą informaciją (bent 3 savybes). Į list įdėkite bent 3 knygas.


# Visas šias knygas išsiveskite. Tuomet parodykite pirmą knygą. Antros
# knygos kažkurią savybę.

# knygos = [
#     {
#         "pavadinimas": "Pradžių pradžia",
#         "autorius": "John Doe",
#         "leidimo_metai": 1999,
#         "zanras": "Fantastika",
#         "puslapiu_skaicius": 350
#     },
#     {
#         "pavadinimas": "Amžių paslaptys",
#         "autorius": "Jane Smith",
#         "leidimo_metai": 2015,
#         "zanras": "Detektyvas",
#         "puslapiu_skaicius": 280
#     },
#     {
#         "pavadinimas": "Kelionė į nežinomybę",
#         "autorius": "Emily Clark",
#         "leidimo_metai": 2020,
#         "zanras": "Nuotykių",
#         "puslapiu_skaicius": 420
#     }
# ]
#
# # Atvaizduojamas sąrašas
# for knyga in knygos:
#     print(f"Pavadinimas: {knyga['pavadinimas']}, Autorius: {knyga['autorius']}, Leidimo metai: {knyga['leidimo_metai']}")
#
# print('Pirma knyga\n', knygos[1])
#
# print('Antros knygos autorius: ', knygos[1]['autorius'])
#
# # 13
#
# # 13.Susikurkite sąrašą, kuriame būtų keletas prekių (kaip dictionary V
# # elementai) ir jį užpildykite pasirinktais duomenimis. V
# # Išveskite visų prekių pavadinimus su kainomis ir dar kokiais nors atributais atskirose eilutėse.

# prekes = [
#     {
#         'pavadinimas': 'Telefonas',
#         'kaina': 1000,
#         'kiekis': 20
#     },
#     {
#         'pavadinimas': 'Laptopas',
#         'kaina': 2000,
#         'kiekis': 40
#     },
#     {
#         'pavadinimas': 'elektronine knyga',
#         'kaina': 400,
#         'kiekis': 12
#     }
# ]
#
# for preke in prekes:
#     print(preke)

# 14

# 14.Susikurkite sąrašą, kuriame būtų saugoma informacija apie keletą
# automobilių (kaip dictionary elementai) ir užpildykite jį pasirinktais
# duomenimis.
# Išveskite kiekvieno automobilio pavadinimą, metus ir
# paskaičiuotą jo amžių (dabartiniai metai - gamybos metai).

from datetime import date

# cars = [
#     {
#         "marke": "Toyota",
#         "modelis": "Corolla",
#         "metai": 2018,
#         "spalva": "balta",
#         "kaina": 12000
#     },
#     {
#         "marke": "BMW",
#         "modelis": "X5",
#         "metai": 2020,
#         "spalva": "juoda",
#         "kaina": 35000
#     },
#     {
#         "marke": "Honda",
#         "modelis": "Civic",
#         "metai": 2016,
#         "spalva": "pilka",
#         "kaina": 9000
#     },
#     {
#         "marke": "Audi",
#         "modelis": "A4",
#         "metai": 2019,
#         "spalva": "raudona",
#         "kaina": 15000
#     },
#     {
#         "marke": "Ford",
#         "modelis": "Mustang",
#         "metai": 2021,
#         "spalva": "mėlyna",
#         "kaina": 45000
#     }
# ]
# amzius = 0
#
# for car in cars:
#     print(f'Automobilio marke: {car['marke']}, metai: {car['metai']}')
#     amzius = datetime.date.today().year - car['metai']
#     print(f'Siam automobiliui: {amzius} metai')
