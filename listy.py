# #1
# lista = []
# lista.append(21)
# lista.append(4)
# lista.append(37)
# print(lista)
#
# #2
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.extend(list2)
# print(list1)
#
# #3
# my_list = [1, 2, 3, 4, 2]
# my_list.pop(1)
# print(my_list)
# my_list.pop()
# print(my_list)
#
# #4
# my_list = [10, 20, 40, 30, 20]
# forty = my_list.index(40)
# print(forty)
#
# #5
# my_list = [1, 2, 2, 3, 2, 4, 2]
# dwojki = my_list.count(2)
# print(dwojki)
#
# -----------------

# #1
# miasto = {
#     "nazwa": "Kraków",
#     "województwo": "Małopolskie",
#     "populacja": 807000,
#     "kraj": "Polska"
# }
#
# klucze = miasto.keys()
# wartosci = miasto.values()
# print(klucze)
# print(wartosci)
from collections import Counter
#2
loty = [{
    "samolot": "Boeing",
    "kierunek": "Warszawa",
    "cena": 250,
    "pasażerowie": 125,
    "liczba_miejsc": 125
},
{
    "samolot": "Airbus",
    "kierunek": "Londyn",
    "cena": 750,
    "pasażerowie": 300,
    "liczba_miejsc": 300
},
{
    "samolot": "Airbus",
    "kierunek": "Poprad-Tatry",
    "cena": 100,
    "pasażerowie": 8,
    "liczba_miejsc": 100
}]

# samoloty = [lot["samolot"] for lot in loty]
# print(samoloty)
# tanie_loty = [lot for lot in loty if lot["cena"] < 500]
# print(tanie_loty)
# do_londynu = [lot for lot in loty if lot["kierunek"] == "Londyn"]
# print(do_londynu)
#
# miejsca = [lot["liczba_miejsc"] for lot in loty]
# print(miejsca)
# suma_miejsc = sum(miejsca)
# print(suma_miejsc)
#
# #1
# pax = [lot["pasażerowie"] for lot in loty]
# suma_pax = str(sum(pax))
# print(suma_pax)
#
# #2
# kierunki = [lot["kierunek"] for lot in loty]
# print(kierunki)
#
# #3
# zysk = [lot["cena"] * lot["pasażerowie"] for lot in loty]
# zysk_sum = sum(zysk)
# print(zysk)
# print(zysk_sum)
#
# #5
# for lot in loty:
#     lot["dostepne_miejsca"] = lot["liczba_miejsc"] > lot["pasażerowie"]
#
# wolne = [lot for lot in loty if lot["dostepne_miejsca"]]
# print(wolne)

samoloty = Counter([lot["samolot"] for lot in loty])
slownik_samolotow = dict(samoloty)
for klucz,wartosc in slownik_samolotow.items():
    print(f"Model {klucz}, ilość {wartosc} sztuk.")