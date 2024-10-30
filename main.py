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

automobilis = {}

automobilis["marke"] = "Toyota"
automobilis["modelis"] = "Supra mk4"
automobilis["rida"] = 85600
automobilis["gamybos_metai"] = 1993
automobilis["spalva"] = "juoda"
automobilis["darbinis_turis"] = 3.0
automobilis["ar_dauzta"] = False
automobilis["ar_parduodama"] = True

print(automobilis)

metu = datetime.date.today().year - automobilis['gamybos_metai']
print(f"Metų skaičius nuo pagaminimo: {metu}")

print(f'Vidutiniskai masina nuvaziavo per metus: {automobilis["rida"] / metu} kilometru')

# 6
