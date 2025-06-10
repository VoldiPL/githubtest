from time import sleep

import requests
import webbrowser

######
# 1. Pobieranie danych o pogodzie (OpenWeatherMap API)
#
# Cel: Nauczyć się wysyłać zapytanie GET i odczytać dane JSON.
#
# Zadanie:
#
#     Zarejestruj się na https://openweathermap.org/api
#
#     Uzyskaj klucz API
#
#     Pobierz aktualną pogodę dla swojego miasta
#
#     Wyświetl: temperaturę, wilgotność, opis pogody
######

API_KEY = "a63369aed57992e5a80f5d62f4f74218"

owm_url = f"http://api.openweathermap.org/geo/1.0/direct?q=Cracow,PL&appid={API_KEY}"
response = requests.get(owm_url)
owm_data = response.json()

lat = owm_data[0]['lat']
lon = owm_data[0]['lon']

url_owm = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
response = requests.get(url_owm)
data_owm = response.json()

weather = {
    "Temperatura": round(data_owm['main']['temp'],1),
    "Wilgotność": data_owm['main']['humidity'],
    "Opis": data_owm['weather'][0]['description']
}

print("Pogoda w Krakowie:"), sleep(0.8)
print(f"* temperatura powietrza to {weather['Temperatura']} st. C"), sleep(0.8)
print(f"* wilgotność powietrza wynosi {weather['Wilgotność']} %"), sleep(0.8)
print(f"* opis zachmurzenia: {weather['Opis']}."), sleep(0.8)
print("***")
sleep(1)

######
######
# daję wyżej żeby było śmiesznie
# 🔹 5. API Chuck Norris Jokes
#
# Cel: Praktyka z endpointami i kategoriami.
#
# Zadanie:
#
#     Użyj: https://api.chucknorris.io/jokes/random
#
#     Możesz też użyć endpointa https://api.chucknorris.io/jokes/categories
#
#     Pobierz losowy dowcip z wybranej kategorii

chuck_cat = "https://api.chucknorris.io/jokes/categories"
chuck_response = requests.get(chuck_cat)
chuck_json = chuck_response.json()

print("Żarty o Chucku Norrisie\n")
value = int(input("Wybierz kategorię dowcipu (0 - 15):"))
chuck_joke_url = f"https://api.chucknorris.io/jokes/random?category={chuck_json[value]}"
chuck_joke_response = requests.get(chuck_joke_url)
chuck_joke_json = chuck_joke_response.json()
print(f"Category is: {str(chuck_json[value]).upper()}.\n"), sleep(2)
print(chuck_joke_json['value']), sleep(3)
print("🤣"), sleep(1)
print("***\n")
sleep(2)

######
######
# 🔹 2. API z dowcipami (Official Joke API)
#
# Cel: Praca z prostym publicznym API.
#
# Zadanie:
#
#     Użyj: https://official-joke-api.appspot.com/random_joke
#
#     Pobierz i wypisz: setup i punchline
#####

joke_url = "https://official-joke-api.appspot.com/random_joke"
joke_response = requests.get(joke_url)
joke_data = joke_response.json()

joke_setup = joke_data['setup']
joke_punch = joke_data['punchline']

print("Uwaga! Losowy żart z internetu:")
sleep(3)
print(joke_setup)
sleep(5)
print(joke_punch)
sleep(3)
print("🤣")
sleep(1)
print("\nPA TERA!")
sleep(1)

######
######
# 🔹 3. API kotków lub piesków
#
# Cel: Pobieranie obrazków z API.
#
#     Kotki: https://api.thecatapi.com/v1/images/search
#
#     Pieski: https://dog.ceo/api/breeds/image/random
#
# Zadanie:
#
#     Pobierz losowy obrazek
#
#     Wyświetl go w przeglądarce (webbrowser.open(url))

cats_url = "https://api.thecatapi.com/v1/images/search"
dogs_url = "https://dog.ceo/api/breeds/image/random"
cats_response = requests.get(cats_url)
dogs_response = requests.get(dogs_url)
cats_data = cats_response.json()
dogs_data = dogs_response.json()


random_cat = webbrowser.open(cats_data[0]['url'])
sleep(3)
random_dog = webbrowser.open(dogs_data['message'])

######
######
# 🔹 4. API wyszukiwania książek (Google Books API)
# 
# Cel: Wysyłanie zapytań z parametrami.
# 
# Zadanie:
# 
#     Użyj: https://www.googleapis.com/books/v1/volumes?q=python
# 
#     Wypisz tytuły i autorów pierwszych 5 książek
######
#
# books_url = "https://www.googleapis.com/books/v1/volumes"
# books_params = {
#     "q": "python",
#     "maxResults": 5
# }
#
# books_response = requests.get(books_url, books_params)
#
# # Sprawdź, czy się udało
# if books_response.status_code == 200:
#     books_data = books_response.json()
#     books = books_data.get("items", [])
#
#
#     for i, book in enumerate(books, 1):
#         info = book.get("volumeInfo", {})
#         title = info.get("title", "brak tytułu")
#         subtitle = info.get("subtitle", "")
#         authors = info.get("authors", ["Nieznany autor"])
#         print(f'{i}. "{title} - {subtitle}", {', '.join(authors)}')
# else:
#     print("Błąd pobierania danych:", books_response.status_code)


