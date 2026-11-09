
zadania = []

while True:
    print("\n1. Dodaj zadanie")
    print("2. Wyswietl zadania")
    print("3. Usun zadanie")
    print("4. Liczba zadan")
    print("0. Zakoncz")

    wybor = int(input("Wybierz opcje: "))

    if wybor == 1:
        zadanie = input("Podaj zadanie: ")
        zadania.append(zadanie)

    elif wybor == 2:
        if len(zadania) == 0:
            print("Brak zadan")
        else:
            for i in range(len(zadania)):
                print(f"{i + 1}. {zadania[i]}")

    elif wybor == 3:
        if len(zadania) == 0:
            print("Brak zadan")
        else:
            numer = int(input("Podaj numer zadania: "))

            if 1 <= numer <= len(zadania):
                zadania.pop(numer - 1)
                print("Zadanie usuniete.")
            else:
                print("Nieprawidlowy numer zadania.")

    elif wybor == 4:
        print("Liczba zadan:", len(zadania))

    elif wybor == 0:
        print("Do widzenia!")
        break

    else:
        print("Nieprawidlowa opcja.")
