print("To test mądrości. Uzupełnij go, a dowiesz się, czy jesteś mądry!")
while True:
    imie = input("Podaj swoje imię: ")
    nametest = imie.isalpha() == True
    if nametest:
        try:
            wiek = int(input(f"Cześć, {imie.title()}! Napisz, ile masz lat: "))
            if wiek < 19:
                input("Do szkoły, gówniarzu! [ENTER]")
            elif 19 <= wiek < 30:
                input("Zaraz sprawdzimy Twoją wiedzę! [ENTER]")
            elif 30 <= wiek < 60:
                input("Mówią, że mądrość przychodzi z wiekiem... [ENTER]")
            elif 60 <= wiek < 110:
                input("STARY A MĄDRY CZY STARY A GŁUPI? [ENTER]")
            else:
                print("Do grobu, a nie do komputera!")
        except:
            print("Wiek musi być liczbą! Spróbuj ponownie.")
            exit()
        q1 = int(input("Podaj rozwiązanie zadania: 2 x 2 = ? "))
        if q1 == 4:
            print(f"\nPrzykro mi, {imie.title()}. Jesteś gupi (:")
        else:
            print("\nJest gorzej, niż myślałem...")
        print("Dziękujemy za skorzystanie z naszego testu!")
        exit()
    else:
        print("Dane niepoprawne. Spróbuj ponownie.")
exit()

