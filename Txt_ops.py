plik = open("test.txt", "a", encoding="utf-8")

if plik.writable():
    ile = plik.write(input("Wprowadź tekst: ") + "\n")
    print("Zapisano: ", ile)
plik.close()

plik = open("test.txt", "r", encoding="utf-8")

if plik.readable():
    print("Zawartość pliku:")
    for l in plik:
        print(l)
