#1
from os.path import split

py = "python"
print(py.title())

#2
slowo = "ananas"
print(slowo.count('a'))

#3
kot = "kot"
tok = kot[::-1]
print(tok)

#4
input = "kajak"
palindrom = input[::-1]
print(input == palindrom)

#5
zdanie = "Ala ma kota"
print(zdanie.replace(" ","-"))

#6
def suma_cyfr(liczba):
    return sum(int(cyfra) for cyfra in str(abs(liczba)))

# Przykład użycia
input_liczba = 2222
wynik = suma_cyfr(input_liczba)
print("Suma cyfr:", wynik)

#7
liczba = 42
reszta = liczba % 2
if reszta == 0:
    print("Ta liczba jest parzysta.")
else:
    print("Ta liczba jest nieparzysta.")

#8
import math
print(math.factorial(5))

#9
liczba = 10
binary = bin(liczba)
print(binary)

#10
def max_cyfra(liczba):
    return max(int(cyfra) for cyfra in str(abs(liczba)))

input_liczba = 9582
wynik = max_cyfra(input_liczba)
print("Największa cyfra to:", wynik)

#11
zdanie = "To jest przykładowe zdanie"
print(len(zdanie.split()))

#12
def usun_cyfry(napis):
  nowy_napis = ""
  for znak in napis:
    if not znak.isdigit():
      nowy_napis += znak
  return nowy_napis

napis = "abc123def456"
napis_bez_cyfr = usun_cyfry(napis)
print(napis_bez_cyfr)

#13
string_one = "Python 3"
string_two = "Python"
print(string_one.isalpha())
print(string_two.isalpha())