#1
imie = "Jan"
nazwisko = "Kowalski"
miasto = "Poznań"

wynik = f"To jest {imie} {nazwisko}. Jego miejsce urodzenia to {miasto}."
print(wynik)

#2
result = "to jest krótkie zdanie na temat Jana"
result_myslnik = result.replace(" ","-")
print(result_myslnik)

#3
greeting = "hello world"

#3a
dlugosc = len(greeting)
print(dlugosc)

#3b
duze_litery = greeting.upper()
print(duze_litery)

#3c
duza_pierwsza = greeting.capitalize()
print(duza_pierwsza)

#4
movie = "lord of the rings"
movie_title = movie.title()
print(movie_title)

#5
day = "dzisiaj jest sobota"
fifth = day[4]
print(fifth)