# # warunki = "aaa"
# #
# # if warunki == "warunki":
# #     print("Warunki są spoko")
# # elif warunki == 3:
# #     print(warunki)
# # else:
# #     print("Cos poszlo nie tak")
#
# #1
# user_role = "admin"
# is_logged = True
#
# if user_role == "admin" and is_logged == True:
#     print("Witaj w panelu admina")
# elif user_role == "mod" and is_logged == True:
#     print("Witaj w panelu moderatora")
# elif user_role == "user" and is_logged == True:
#     print("Witaj w panelu użytkownika")
# else:
#     print("Błąd logowania")
#
# #2
# user_country = "PL"
#
# if user_country == "PL" or user_country == "DE" or user_country == "CZ":
#     print("Złóż zamówienie")
# else:
#     print("Dostawa niemożliwa")
#
# #3
# import time
# t = time.localtime()
# current_time = time.strftime("%H",t)
# cti = int(current_time)
# if cti >= 6 and cti <= 12:
#     print("Good morning")
# elif cti >= 12 and cti <= 18:
#     print("Good afternoon")
# elif cti >= 18:
#     print("Good evening")
# else:
#     print("Do spania! :)")
#
# #alt 2
# countries = ["PL","DE","CZ"]
# user_country = "PL"
#
# if user_country in countries:
#     print("Złóż zamówienie")
# else:
#     print("Dostawa niemożliwa")

#1
lang = "Python"
match(lang):
    case "Python":
        print("Backend")
    case "PHP":
        print("Backend")
    case "Java":
        print("Backend")
    case "Javascript":
        print("Frontend")
    case "HTML":
        print("Frontend")
    case _:
        print("Nie rozpoznano!")

#2
import datetime

teraz = datetime.datetime.now()
month = int(teraz.month)

match(month):
    case 1:
        print("Styczeń")
    case 2:
        print("Luty")
# [...]
    case 5:
        print("Maj")
    case 8:
        print("Sierpień")
# i tak dalej

# #3
# Napisz słownik (dictionary) z kluczami, imię,nazwisko, wiek
# 
# w try except spróbuj wyprintować klucz który nie istnieje np. miasto
#
# napisz except, który obsłuży błąd klucza (nie istniejący klucz)
osoba = {
    "imie": "Bartosz",
    "nazwisko": "Zakroczymski",
    "wiek": 30}

try:
    print(osoba["miasto"])
except KeyError:
    print("Błąd: Podany klucz nie istnieje w słowniku.")