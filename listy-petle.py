# 📦 Ćwiczenie 1: Wypisz wszystkie klucze i wartości ze słownika

# user = {
#     "name": "Anna",
#     "age": 30,
#     "email": "anna@example.com"
# }
#
# for key,value in user.items():
#     print(f"{key}: {value}")

# 🔢 Ćwiczenie 2: Oblicz średni wiek użytkowników

# users = {
#     "user1": {"name": "Anna", "age": 30},
#     "user2": {"name": "Bartek", "age": 25},
#     "user3": {"name": "Celina", "age": 35}
# }
#
# print(users.values())
# total_age = 0
#
# for user in users.values():
#     total_age += user['age']
#     print(total_age)
#
# avg = total_age / len(users)
# print(avg)
# print("*")

# 🔍 Ćwiczenie 3: Znajdź użytkownika z największym wiekiem

# users = {
#     "u1": {"name": "Kasia", "age": 20},
#     "u2": {"name": "Tomek", "age": 40},
#     "u3": {"name": "Asia", "age": 35}
# }
#
# oldest_user = None
# age = 0
# for user in users.values():
#     if user['age'] > age:
#         age = user['age']
#         oldest_user = user['name']
#
# print(f"Najstarszy: {oldest_user}, ma {age} lat.")

# 🌐 Ćwiczenie 4: Symulacja odpowiedzi z API (lista słowników)

# Udawana odpowiedź z API
posts = [
    {"id": 1, "title": "Witaj świecie", "likes": 10},
    {"id": 2, "title": "Drugi post", "likes": 3},
    {"id": 3, "title": "Python i API", "likes": 20}
    ]

for post in posts:
    print(f'"{post['title']}", polubień: {post['likes']}.')
print("***")
# ✅ Ćwiczenie 5: Filtruj dane z API – tylko popularne posty

for post in posts:
    if post['likes'] > 5:
        print(f'"{post['title']}", polubień: {post['likes']}.')

# 🧩 Ćwiczenie 6: Tworzenie własnego słownika z list

# Dane z API: dwie listy
names = ["Anna", "Bartek", "Celina"]
emails = ["anna@example.com", "bartek@example.com", "celina@example.com"]

# Zrób z tego listę słowników użytkowników
users = []
for i in range(len(names)):
    users.append({"name": names[i],
                  "email": emails[i]})

print(users)

# Jakieś moje pierdololo

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

dane = []

for osoba in osoby:
    dana = (f"{osoba['imię'][:4].lower()}.{osoba['nazwisko'][:3].lower()}")
    dane.append(dana)

print(dane[0])

