# 1. Susikurkite tuple iš studijų programos modulių pavadinimų.
# Atspausdinkite šiuos pavadinimus sąraše, prieš kiekvieną pavadinimą
# išvedant brūkšniuką. Raskite ilgiausią modulio pavadinimą.

# Ka padaryti?

tuple = ('tuples', 'dictionaries', 'sets')
for x in tuple:
    print(f'-{x}')

print(max(map(len,tuple)))

longest_name = max(tuple, key=len)
print(longest_name)

# Susikurkite tuple iš mėnesių pavadinimų. Susikurkite kitus tuples
# sezonams apibūdinti: žiema, pavasaris, vasara, ruduo. Panaudokite slicing
# [start:end], kad atitinkamus mėnesius sudėtumėte į atitinkamus sezonų
# tuples. Šį priskyrimą turite atlikti kuriant individualius sezonų tuples, kitaip
# išmes klaidą, kad jo negalite modifikuoti.

menesiai = ('sausis', 'vasaris', 'kovas',
'balandis', 'geguze', 'birzelis', 'liepa',
'rugpjutis', 'rugsejis', 'spalis', 'lapkritis',
'gruodis')

print(f'Spring: {menesiai[2:5]}')
print(f'Summer: {menesiai[5:8]}')
print(f'Autumn: {menesiai[8:11]}')
print(f'Winter: {menesiai[11:12] + menesiai[0:2]}')

