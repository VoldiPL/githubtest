# liczby = [0,21,34,134,36,243,54,877]
#
# for i in liczby:
#     if i % 2 != 0:
#         continue
#     print(f"Liczby nieparzyste tego zbioru to {i}")

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

#5 DO ZROBIENIA, DO TEGO 6 Z DISCORDA
# slowo = input("Podaj JEDEN wyraz: ")
# palindrom = slowo[::-1]
#
#     if slowo == palindrom:
#         print("To jest palindrom")
#     else:
#         print("To nie jest palindrom")

#7 - BANK
stan_konta = 5000

while True:
    print("--Witamy w aplikacji--")
    print("1. Podaj stan konta")
    print("2. Wpłać pieniądze")
    print("3. Wypłać środki")
    print("4. Wyzeruj stan konta")
    print("5. Zakończ")

    operacja = int(input("Wybierz operację: "))

    match operacja:
        case 1:
            print(f"Stan konta to: {stan_konta}.\n")
        case 2:
            kwota = int(input("Wpisz kwotę do wpłaty: "))
            stan_konta += kwota
            print(f"Wpłacono {kwota} zł.\n")
        case 3:
            kwota = int(input("Wpisz kwotę do wypłacenia: "))
            stan_konta -= kwota
            print(f"Wypłacono {kwota} zł.\n")
        case 4:
            stan_konta = 0
            print(f"Stan konta to: {stan_konta}.\n")
        case 5:
            print("Dziękujemy za skorzystanie z aplikacji :)")
            break