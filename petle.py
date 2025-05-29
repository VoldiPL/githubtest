# liczby = [0,21,34,134,36,243,54,877]
#
# for i in liczby:
#     if i % 2 != 0:
#         continue
#     print(f"Liczby nieparzyste tego zbioru to {i}")
# from operator import index
#
# from listy_hw import najwieksza

# #1
# imiona = ["Krzysztof","Andrzej","Joanna","Mariusz","Barbara"]
# for name in imiona:
#     print(f"Cześć, tu {name}.")
#
# #2
# for i in range(10,250):
#     if i % 7 != 0:
#         continue
#     print(i)
#
# #3
# for i in range(0,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(f"{i} - FizzBuzz")
#     elif i % 3 == 0:
#         print(f"{i} - Fizz")
#     elif i % 5 == 0:
#         print(f"{i} - Buzz")
#     else:
#         print(i)
#
# #4
# zdanie = input("Podaj zdanie do sprawdzenia: ")
# litera = input("Teraz podaj literę: ")
#
# for znak in zdanie:
#     znaki = zdanie.count(litera)
# print(f"Ta litera występuje {znaki} razy.")

#5 z pomocą GPT
# wyraz = input("Podaj JEDEN wyraz: ").lower()
# # Pobieranie wyrazu od użytkownika
#
# czy_palindrom = True
# dlugosc = len(wyraz)
#
# for i in range(dlugosc // 2):
#     if wyraz[i] != wyraz[dlugosc - 1 - i]:
#         czy_palindrom = False
#         break
#
# if czy_palindrom:
#     print("To jest palindrom.")
# else:
#     print("To nie jest palindrom.")

#6 Napisz program, który:
# Pobiera od użytkownika ciąg liczb całkowitych (oddzielonych spacją).
# Zamienia je na listę liczb.
# Za pomocą pętli znajduje:
# największą liczbę i jej indeks w liście,
# najmniejszą liczbę i jej indeks w liście.
# Wyświetla te wartości i ich indeksy.

# txt = input("Podaj ciąg liczb (oddziel SPACJĄ): ")
# lista_str = txt.split()
# lista_int = list(map(int,lista_str))
# print("Podane liczby to: ", lista_int)
# max_num = max(lista_int)
# ind_max = lista_int.index(max_num)
# min_num = min(lista_int)
# ind_min = lista_int.index(min_num)
# print(f"Największa liczba z tej listy to: {max_num}. Jej indeks w liście to {ind_max}.")
# print(f"Najmniejsza liczba z tej listy to: {min_num}. Jej indeks w liście to {ind_min}.")

#2 z githuba
# Zmienne określające liczby parzyste i nieparzyste
parzyste = 0
nieparzyste = 0

# Pętla for od 1 do 100 (włącznie)
for i in range(1, 101):
    if i % 2 == 0:
        parzyste += 1
    else:
        nieparzyste += 1

# Wyświetlenie wyników
print("Liczby parzyste:", parzyste)
print("Liczby nieparzyste:", nieparzyste)


#7 - BANK
# stan_konta = 5000
#
# while True:
#     print("--Witamy w aplikacji--")
#     print("1. Podaj stan konta")
#     print("2. Wpłać pieniądze")
#     print("3. Wypłać środki")
#     print("4. Wyzeruj stan konta")
#     print("5. Zakończ")
#
#     operacja = int(input("Wybierz operację: "))
#
#     match operacja:
#         case 1:
#             print(f"Stan konta to: {stan_konta}.\n")
#         case 2:
#             kwota = int(input("Wpisz kwotę do wpłaty: "))
#             stan_konta += kwota
#             print(f"Wpłacono {kwota} zł.\n")
#         case 3:
#             kwota = int(input("Wpisz kwotę do wypłacenia: "))
#             stan_konta -= kwota
#             print(f"Wypłacono {kwota} zł.\n")
#         case 4:
#             stan_konta = 0
#             print(f"Stan konta to: {stan_konta}.\n")
#         case 5:
#             print("Dziękujemy za skorzystanie z aplikacji :)")
#             break