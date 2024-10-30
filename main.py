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

knyga1 = {
    "pavadinimas": "Vėjų medžiotojai",
    "autorius": "Jonas Pavardė",
    "žanras": "Nuotykinė literatūra",
    "kaina": 15.99,
    "puslapių kiekis": 320,
    "skyriai": ["Pradžia", "Kelionės pradžia", "Audros", "Nuotykiai jūroje", "Atrastos paslaptys", "Pabaiga"],
    "išleidimo metai": 2021,
    "galima rasti knygynuose": True
}

knyga2 = {
    "pavadinimas": "Laiko šešėliai",
    "autorius": "Viktorija Raštaitė",
    "žanras": "Fantastika",
    "kaina": 19.49,
    "puslapių kiekis": 420,
    "skyriai": ["Laiko įvadas", "Magiškos būtybės", "Tamsos užtemimas", "Drąsos išbandymas", "Galutinė kova", "Atgimimas"],
    "išleidimo metai": 2018,
    "galima rasti knygynuose": False
}

print(knyga1)
print(knyga2)

if knyga2['puslapių kiekis'] > knyga1['puslapių kiekis']:
    print('Pirma knyga plonesne')
elif knyga2['puslapių kiekis'] < knyga1['puslapių kiekis']:
    print('Antra knyga plonesne')
else:
    print('Pusplaiu skaicius vienodas')

count1 = 0
count2 = 0

for x in knyga1['skyriai']:
    count1 += 1

for u in knyga2['skyriai']:
    count2 += 1

if count1 > count2:
    print('Pirma knyga turi daugiau skyriu')
if count1 < count2:
    print('Antra knyga turi daugiau skyriu')
else:
    print('Lygus skyriu skaicius')

if knyga1['kaina'] > knyga2['kaina']:
    print('Knyga pirma yra brangesne')
    dviguba = knyga2['kaina'] * 2
    if dviguba > knyga1['kaina']:
        print('Padvigubinta suma antros knygos, butu brangesne uz pirmos knygos kaina')
if knyga1['kaina'] < knyga2['kaina']:
    print('Knyga antra yra brangesne')
    dviguba = knyga1['kaina'] * 2
    if dviguba > knyga2['kaina']:
        print('Padvigubinta suma pirmos knygos, butu brangesne uz antros knygos kaina')
