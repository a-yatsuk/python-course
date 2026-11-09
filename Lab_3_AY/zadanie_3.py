ksiazki = []

while True:
    print("""
================ Biblioteka ================
1. Dodaj ksiazke
2. Wyswietl wszystkie ksiazki
3. Wypozycz ksiazke
4. Zwroc ksiazke
5. Usun ksiazke
0. Zakoncz
""")

    opcja = input("Wybierz opcje: ").strip()

    if opcja not in ["0", "1", "2", "3", "4", "5"]:
        print("Nieprawidlowa opcja.")
        continue

    if opcja == "0":
        break

    elif opcja == "1":
        tytul = input("Tytul: ").strip()
        autor = input("Autor: ").strip()

        if not tytul or not autor:
            print("Tytul i autor nie moga byc puste.")
            continue

        ksiazka = {
            "tytul": tytul,
            "autor": autor,
            "dostepna": True
        }

        ksiazki.append(ksiazka)
        print("Ksiazka dodana.")

    elif opcja == "2":
        if not ksiazki:
            print("Katalog jest pusty.")
        else:
            for i in range(len(ksiazki)):
                ksiazka = ksiazki[i]

                if ksiazka["dostepna"]:
                    status = "Dostepna"
                else:
                    status = "Wypozyczona"

                print(
                    i + 1,
                    ksiazka["tytul"],
                    "-",
                    ksiazka["autor"],
                    "-",
                    status
                )

    elif opcja in ["3", "4", "5"]:
        if not ksiazki:
            print("Katalog jest pusty.")
            continue

        numer = input("Numer ksiazki: ").strip()

        if not numer.isdecimal():
            print("Nieprawidlowy numer.")
            continue

        numer = int(numer)

        if numer < 1 or numer > len(ksiazki):
            print("Nie ma ksiazki o takim numerze.")
            continue

        ksiazka = ksiazki[numer - 1]

        if opcja == "3":
            if ksiazka["dostepna"]:
                ksiazka["dostepna"] = False
                print("Wypozyczono:", ksiazka["tytul"])
            else:
                print("Ta ksiazka jest juz wypozyczona.")

        elif opcja == "4":
            if not ksiazka["dostepna"]:
                ksiazka["dostepna"] = True
                print("Zwrocono:", ksiazka["tytul"])
            else:
                print("Ta ksiazka nie jest wypozyczona.")

        elif opcja == "5":
            del ksiazki[numer - 1]
            print("Usunieto:", ksiazka["tytul"])
                



