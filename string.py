# # Typ prosty: string
#
# imie = "Jan"
# nazwisko = 'Kowalski'
# tekst = f"To jest tekst {2 + 5}"
#
# typ = type(nazwisko)
#
# kraj = "Polska"
# stolica = "Warszawa"
#
# informacja = "To jest " + kraj + ". Stolica to " + stolica + "."
# info = f"To jest {kraj}. Stolica to {stolica}."
#
# cytat = 'To jest "cytat" z książki'
# print(cytat)

film = "Harry Potter i Komnata Tajemnic"

duza_litera = film.upper()
mala_litera = film.lower()
inny_film = film.replace("R","?")
url = film.replace(" ","-").lower()

pierwsza_litera = film[0]

spacje = "  dawid"
bez_spacji = spacje.strip()

zakres = film[6:12]
print(zakres)

