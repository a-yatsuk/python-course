kontakty = {}

while True:
    print("""
========== KSIAZKA KONTAKTOW ==========
1. Dodaj kontakt
2. Wyswietl wszystkie kontakty
3. Wyszukaj kontakt
4. Edytuj kontakt
5. Usun kontakt
0. Zakoncz
=======================================
""")

    opcja = input("Wybierz opcje: ")

    if opcja == "1":
        imie = input("Imie: ")
        nazwisko = input("Nazwisko: ")
        telefon = input("Telefon: ")

        if telefon in kontakty:
            print("Kontakt z tym numerem juz istnieje.")
        else:
            kontakty[telefon] = [imie, nazwisko]
            print("Kontakt dodany.")

    elif opcja == "2":
        if not kontakty:
            print("Ksiazka kontaktow jest pusta.")
        else:
            for telefon, dane in kontakty.items():
                print(dane[0], dane[1], "- Telefon:", telefon)

    elif opcja == "3":
        telefon = input("Podaj numer telefonu: ")

        if telefon in kontakty:
            dane = kontakty[telefon]
            print(dane[0], dane[1], "- Telefon:", telefon)
        else:
            print("Nie znaleziono kontaktu.")

    elif opcja == "4":
        telefon = input("Podaj numer telefonu: ")

        if telefon in kontakty:
            imie = input("Nowe imie: ")
            nazwisko = input("Nowe nazwisko: ")
            kontakty[telefon] = [imie, nazwisko]
            print("Kontakt zmieniony.")
        else:
            print("Nie znaleziono kontaktu.")

    elif opcja == "5":
        telefon = input("Podaj numer telefonu: ")

        if telefon in kontakty:
            del kontakty[telefon]
            print("Kontakt usuniety.")
        else:
            print("Nie znaleziono kontaktu.")

    elif opcja == "0":
        print("Koniec programu.")
        break

    else:
        print("Nieprawidlowa opcja.")
         
