import csv

#scrierea unui dictionar in csv
# header = ['name', 'age', 'country']
#
# rows = [{'name': 'George', 'age': 29, 'country': 'Turcia'},
#         {'name': 'Diana', 'age': 27, 'country': 'Romania'},
#         {'name': 'Teodora', 'age': 26, 'country': 'Franta'},
#         {'name': 'Tudor', 'age': 56, 'country': 'Belgia'},
#         {'name': 'Andrei', 'age': 33, 'country': 'Elvetia'}]
#
# with open('countries_csv', 'w', newline='') as f:
#     writer = csv.DictWriter(f, fieldnames=header)
#     writer.writeheader()
#     writer.writerows(rows)
#
# #scrierea unei liste in csv
#
# header = ['name', 'age', 'country']
#
# rows = [['ana', 20, 'grecia'],
#         ['Cristi', 22, 'romania']]
# with open('countries2_csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#     writer.writerows(rows)
#
# with open('countries_csv', 'r') as f:
#     reading = csv.reader(f)
#     for item in reading:
#         print(item)
#
# lista = ['cosmina', 45, 'marte']
# rows.append(lista)
# with open('countries2_csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#     writer.writerows(rows)


# rows.append(lista)
# writer.writerows(lista)


# cap_tabel = ['nume', 'medalii']
# info = [{'nume': 'leila', 'medalii': 4},
#         {'nume': 'vladimir', 'medalii': 10}]
#
# with open('clasament.csv', 'w', newline="") as file:
#     scrie = csv.DictWriter(file, fieldnames=cap_tabel)
#     scrie.writeheader()
#     scrie.writerows(info)

# cap_tabel = ['nume', 'medalii']
# date = [['margareta', 100], ['silviu', 86]]
# #
# with open('clasament.csv', 'w', newline="") as dates:
#     xyz = csv.writer(dates)
#     xyz.writerow(cap_tabel)
#     xyz.writerows(date)

#vad ce am in acel fisier
# with open('clasament.csv', 'r') as informatii:
#     for item in informatii:
#         print(item)














