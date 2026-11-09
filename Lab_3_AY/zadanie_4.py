operacje = []
while True:
    print("""==========MOJ BUDGET==========
    1.Dodaj przychod
    2.Dodaj wydatek
    3.Wyswietl historie operacji
    4.Wyswietl stan konta
    5.Podsumuwanie finansowe
    6.Wyszukaj operacje
    7.Usun operacje
    0. Zakoncz
    """)
    opcja = input('Wybierz opcje: ')

    if opcja not in ["0", "1", "2", "3", "4", "5", "6"]:
        print("Nieprawidlowa opcja.")
        continue

    if opcja == "0":
        break

    elif opcja in ["1", "2"]:
        opis = input("Opis: ")
        tekst = input("Kwota: ").strip().replace(",", ".")

        
        if not tekst.replace(".", "", 1).isdecimal():
            print("Nieprawidlowa kwota.")
            continue

        kwota = float(tekst)

        if kwota <= 0 or kwota == float("inf"):
            print("Kwota musi byc dodatnia i skonczona.")
            continue

        if opcja == "1":
            typ = "Przychod"
        else:
            typ = "Wydatek"

        operacja = {
            "typ": typ,
            "opis": opis,
            "kwota": kwota
        }

        operacje.append(operacja)
        print("Dodano:", typ)

    elif opcja == "3":
        if not operacje:
            print("Historia jest pusta.")
        else:
            for i in range(len(operacje)):
                operacja = operacje[i]

                print(
                    i + 1,
                    operacja["typ"],
                    "-",
                    operacja["opis"],
                    "-",
                    operacja["kwota"],
                    "zl"
                )

    elif opcja in ["4", "5"]:
        suma_przychodow = 0
        suma_wydatkow = 0
        najwiekszy_wydatek = 0

        for operacja in operacje:
            if operacja["typ"] == "Przychod":
                suma_przychodow += operacja["kwota"]
            else:
                suma_wydatkow += operacja["kwota"]

                if operacja["kwota"] > najwiekszy_wydatek:
                    najwiekszy_wydatek = operacja["kwota"]

        bilans = suma_przychodow - suma_wydatkow

        if opcja == "4":
            print("Stan konta:", round(bilans, 2), "zl")

        else:
            print("Suma przychodow:", round(suma_przychodow, 2), "zl")
            print("Suma wydatkow:", round(suma_wydatkow, 2), "zl")
            print("Bilans:", round(bilans, 2), "zl")

            if najwiekszy_wydatek > 0:
                print("Najwiekszy wydatek:", najwiekszy_wydatek, "zl")
            else:
                print("Brak wydatkow.")

    elif opcja == "6":
        if not operacje:
            print("Historia jest pusta.")
            continue

        numer = input("Numer operacji: ")

        if not numer.isdecimal():
            print("Nieprawidlowy numer.")
            continue

        numer = int(numer)

        if numer < 1 or numer > len(operacje):
            print("Nie ma operacji o takim numerze.")
            continue

        del operacje[numer - 1]
        print("Operacja usunieta.")

