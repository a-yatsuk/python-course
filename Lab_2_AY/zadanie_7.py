
magazyn = {"Mysz": 5, "Klawiatura": 3, "Monitor": 2}

while True:
    print("\n1. Stan magazynu")
    print("2. Przyjecie towaru")
    print("3. Wydanie towaru")
    print("0. Zakoncz")

    wybor = int(input("Wybierz opcje: "))

    if wybor == 1:
        for produkt in magazyn:
            print(f"{produkt}: {magazyn[produkt]} szt.")

    elif wybor == 2:
        produkt = input("Nazwa produktu: ")
        liczba = int(input("Liczba sztuk: "))

        if produkt in magazyn:
            magazyn[produkt] += liczba
            print("Zaktualizowano stan produktu.")
        else:
            magazyn[produkt] = liczba
            print("Dodano nowy produkt.")

    elif wybor == 3:
        produkt = input("Nazwa produktu: ")
        liczba = int(input("Liczba sztuk: "))

        if produkt not in magazyn:
            print("Nie ma takiego produktu.")

        elif magazyn[produkt] >= liczba:
            magazyn[produkt] -= liczba
            print(f"Wydano {liczba} szt.")

        else:
            print("Niewystarczajaca liczba sztuk.")

    elif wybor == 0:
        print("Do widzenia!")
        break

    else:
        print("Nieprawidlowa opcja.")
