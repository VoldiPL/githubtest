import requests

# Ćwiczenie 1: Pobierz wszystkie posty
#
#     Wyślij zapytanie GET na endpoint /posts
#
#     Sprawdź, ile postów znajduje się w odpowiedzi
#
#     Wypisz tytuły pierwszych 5 postów

base_url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(base_url)
posts = response.json()
lengh = len(posts)
print(lengh)

for i,post in enumerate(posts[:5]):
    print(f"{i} - {post['title']}")

print("***")

# 👤 Ćwiczenie 2: Pobierz dane jednego użytkownika
#
#     Pobierz dane użytkownika o ID = 1 (/users/1)
#
#     Wypisz jego imię, nazwisko, email i miasto

base_url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(base_url)
users = response.json()
dane = users['name'], users['email'], users['address']['city']
print(dane)

# ✉️ Ćwiczenie 3: Wyszukaj wszystkie komentarze do posta
#
#     Pobierz komentarze do posta o ID = 1 (/posts/1/comments)
#
#     Wypisz imiona komentujących i fragmenty komentarzy

url = "https://jsonplaceholder.typicode.com/posts/1/comments"

response = requests.get(url)
comments = response.json()

for comment in comments:
    print(f"ID: {comment['id']}")
    print(f"Name: {comment['name']}")
    print(f"Comment preview: {comment['body'][:30]}...")
    print("-" * 40)


# 🔍 Ćwiczenie 4: Filtruj posty danego użytkownika
#
#     Pobierz posty użytkownika o ID = 2 (/posts?userId=2)
#
#     Wypisz ich ID i tytuły

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
posts = response.json()

for comment in posts:
    if comment['userId'] == 2:
        print(f"ID: {comment['id']}")
        print(f"Title: {comment['title']}")
        print("-" * 40)
#
# 📦 Ćwiczenie 5: Zapisz dane postów do listy słowników
#
#     Z endpointa /posts wybierz tylko posty, które mają ID < 5
#
#     Utwórz listę słowników zawierających id, title i userId

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
posts = response.json()
selected_posts = []

for post in posts:
    if post['id'] < 5:
        selected_posts.append({
            "id": post['id'],
            'title': post['title'],
            'userId': post['userId']
        })

for post in selected_posts:
    print(post)

#
# 🧠 Ćwiczenie 6: Znajdź użytkownika o największej liczbie postów
#
#     Pobierz wszystkie posty
#
#     Policz, ilu postów napisał każdy użytkownik
#
#     Znajdź użytkownika z największą liczbą postów

post_counts = {}
for post in posts:
    user_id = post['userId']
    if user_id in post_counts:
        post_counts[user_id] += 1
    else:
        post_counts[user_id] = 1

max_posts = 0
top_user_id = None

for user_id, count in post_counts.items():
    if count > max_posts:
        max_posts = count
        top_user_id = user_id

print(f"Użytkownik z największą liczbą postów to userId: {top_user_id}, liczba postów: {max_posts}")

#
# 🔄 Chcesz wersje trudniejsze (np. z API pogodowym, autoryzacją lub zapisem do pliku)?
#
# Daj znać – mogę przygotować też zadania z OpenWeather, GitHub API lub symulowane logowanie/tokeny.