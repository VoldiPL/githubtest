#1
lista = [1, 2, 3, 4, 5]
suma = sum(lista)
spr = 1 + 2 + 3 + 4 + 5
print("#1.", suma)
print("#1. spr.:", spr)
print("#1.", suma == spr)

#2
lista = [15, 3, 10, 4, 22]
najwieksza = max(lista)
print("#2.",najwieksza)

#3
lista = [2, 5, 3, 5, 7, 5]
for num in lista:
    lista.remove(5)
print("#3.",lista)

#4
lista = [1, 2, 3, 4, 5]
new_list = []
for num in lista:
    new_list.append(num * 2)
print("#4.",new_list)

#5
lista = [3, 7, 12, 9, 20]
if 9 in lista:
    print("#5. Liczba 9 znajduje się w liście.")
else:
    print("#5. W tym zbiorze nie znaleziono liczby 9.")

#6
lista = [5, 2, 9, 1, 6, 7]
lista.sort()
print("#6.",lista)

#7
lista = [1,3,8,4,7]
lista.sort(reverse=True)
print("#7.",lista)

#8
lista = [1,2,3,2,4,1,5]
bez_dupl = set(lista)
print("#8.",list(bez_dupl))

#8 alt.
lista = [1,2,3,2,4,1,5]
temp_lista = []

for i in lista:
    if i not in temp_lista:
        temp_lista.append(i)

lista = temp_lista
print("#8a:", lista)

#9
lista = [10, 20, 20, 30, 20, 40]
szukana = 20
count = lista.count(szukana)
print(f"#9. Liczba {szukana} występuje w liście {count} razy.")

#10
lista = [5,15,10,25,8,12]
temp_lista = []

for i in lista:
    if i > 10:
        temp_lista.append(i)
lista = temp_lista
print("#10. Liczby > 10:", lista)

#11
lista = [10,20,30,40,50,60]
parzyste = lista[::2]
print("#11.",parzyste)

#12
lista = [3,5,7,9,2]
avg = sum(lista) / len(lista)
print("#12.", avg)

#13
lista = [1,2,3,4,5]
odwrocona = lista[::-1]
print("#13.", odwrocona)

#14
lista = [1,2,3,4,5]
new_list = []
for num in lista:
    new_list.append(num + 3)
print("#14.",new_list)

#15
lista = [1,2,3,4,5]
lista.insert(2,99)
print("#15.", lista)

#16
lista = [10,20,30,40,50]
lista.pop(3)
print("#16.", lista)

#17
lista = [1,2,3,4,5,6]
parzyste = []

for i in lista:
    if i % 2 == 0:
        parzyste.append(i)
print("#17.", parzyste)

#18
