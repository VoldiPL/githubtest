x = 12
y = 2

try:
    lista = [3]
    print(lista[0])
    print(x + 4)
    print(x / y)
    print("Linijka po")
except (ZeroDivisionError, TypeError):
    print("Wystąpił 1 z 2 błędów!")
except:
    print("Inny błąd!")
finally:
    print("FINALLY: Wykonam się i tak!")

print("...")

osoby = [
    {
    "imię" : "Bartosz",
    "nazwisko" : "Zakroczymski",
    "wiek" : 28
},
{
    "imię" : "Andrzej",
    "nazwisko" : "Przepona",
    "wiek" : 69
}]

try:
    print(osoby[0]["imię"])
except KeyError as err_ke:
    print(f"Nie znaleziono klucza {err_ke}!")
