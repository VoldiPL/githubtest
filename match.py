# w MATCH przypadki CASE powinny układać się
# od najbardziej szczegółowych do najbardziej ogólnych

print("1.")
print("""Kto prowadzi Milionerów?""")
print("A. Tomasz Kammel\t"
      "B. Bogusław Linda\t"
      "C: Hubert Urbański\t"
      "D: Michał Milowicz")

#answer = input("Podaj odpowiedź A B C D: ")
answer = "C"

match answer.upper():
    case "C":
        print("Tak")
    case "A" | "B" | "D":
        print("Nie")
    case _: # tzw. "dzika karta", symbol "_" reprezentuje dowolny obiekt
        print("Niepoprawna odpowiedź")

# -----
print("\n2.")

dane = [5, 5]

match dane:
    case [5, _]:
        print("tak")
    case [_, 4]:
        print("też tak")
    case [5, 4]:
        print("ostateczne tak")
    case _:
        print("nie")

# -----
print("\n3.")
import random

list1 = [0,1,2,3,4,5,"a","b","c"]
a = random.choice(list1)
b = random.choice(list1)
print(f"a = {a}, b = {b}")

dane = (a, b)
match dane:
    case (x, y):
        print("Punkt", x, y)
    case (0, 0):
        print("Punkt 0")
    case (0, _):
        print("Z lewej strony")
    case (_, _):
        print("Inny punkt")

# -----
print("\n4.")

t = (a, b)
print(f"a = {a}, b = {b}")
# Przypisanie wartości x i y ma miejsce PRZED sprawdzeniem warunków
try:
    match t:
        case (x, y) if x < y:
            print(x, "<", y)
        case (x, y) if x > y:
            print(x, ">" ,y)
        case (x, y) if x == y:
            print(x, "=", y)
except:
    print("niepoprawne dane")

# -----
print("\n5.")

t = [9, 9, 3, 9, 1, 9, 9, 2, 3, 0]

# sprawdza, czy lista ma 10 elementów a 2, 4 i 6 z nich jest równa 9
match t:
    case [_, 9, _, 9, _, 9, _, _, _, _]:
        print('tak')

# -----
print("\n6.")

dane = [6, 1, 3, 9, 1, 7, 7, 2, 3, 0]

# jeśli lista ma co najmniej 2 elementy, pozostałe spakuj do zmiennej "a"
match dane:
    case [_, _, *a]:
        print(a)

# -----
print("\n7.")

dane = [5, 1, 3, 9, 1, 7, 7, 2, 3, 0]

# jeśli pierwszy element listy to 5
match dane:
    case [5, *_]:
        print('pierwszy element zbioru to 5')

# jeśli ostatni element listy to 0
match dane:
    case [*_, 0]:
        print('ostatni element zbioru to 0')

# jeśli pierwszy element listy to 5, a ostatni element listy to 0
match dane:
    case [5, *_, 0]:
        print("Pierwszy: 5, ostatni 0")

# --- ZADANIA ---
print("\n --- ZADANIA ---")
print("Zad. 1.")

# Match zwracający dni tygodnia:

days = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
day = random.choice(days)
print(day)

match day:
    case 1:
        print("poniedziałek")
    case 2:
        print("wtorek")
    case 3:
        print("środa")
    case 4:
        print("czwartek")
    case 5:
        print("piątek")
    case 6:
        print("sobota")
    case 7:
        print("niedziela")
    case _:
        print("Tydzień ma 7 dni")

# -----
print("\nZad. 2.")
punkt = (0, 75)
match punkt:
    case (x, y) if x == 0 and y > 50:
        print("cokolwiek")