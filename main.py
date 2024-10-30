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

filmas = {
    'Pavadinimas': 'The Substance',
    'Rezisierius': 'Coralie Fargeat',
    'Biudzetas': ['$', 17.5, 'million'],
    'Uzdarbys': ['$', 39.1, 'million'],
    'Zanras': 'body horror',
    'Ilgis': '141 minutes',
    'Isleidimo metai': [20, 'September', 2024],
    'Aktoriu sarasas': ['Demi Mūr', 'Margaret Qualley', 'Denis Kveidas', 'Hugo Diego Garcia']
}

print(filmas)
pelnas = filmas['Uzdarbys'][1] - filmas['Biudzetas'][1]
print(pelnas)

count = 0

for x in filmas['Aktoriu sarasas']:
    count += 1

print(f'Aktoriu kiekis: {count}')

print(f'Metu filmui: {filmas['Isleidimo metai'][2] - datetime.date.today().year}')