while True:
    print("""
========== KALKULATOR ==========
1. Dodawanie
2. Odejmowanie
3. Mnozenie
4. Dzielenie
5. Potegowanie
6. Srednia z podanych liczb
0. Zakoncz
================================
""")

    opcja = input('Wybierz opcje: ')

    if opcja not in ["0", "1", "2", "3", "4", "5", "6"]:
        print('Nieprawidlowa opcja.')
        continue

    if opcja == "0":
        break

    if opcja in ["1", "2", "3", "4", "5"]:
        n1 = float(input('Wpisz pierwsza liczbe: '))
        n2 = float(input('Wpisz druga liczbe: '))

        if opcja == "1":
            print('Suma:', n1 + n2)

        elif opcja == "2":
            print('Roznica:', n1 - n2)

        elif opcja == "3":
            print('Iloczyn:', n1 * n2)

        elif opcja == "4":
            if n2 == 0:
                print('Nie mozna dzielic przez zero.')
            else:
                print('Iloraz:', n1 / n2)

        elif opcja == "5":
            if n1 == 0 and n2 < 0:
                print('Nie mozna podnosic zera do ujemnej potegi.')
            else:
                print('Potega:', n1 ** n2)

    elif opcja == "6":
        ile = int(input('Ile liczb chcesz podac? '))

        if ile <= 0:
            print('Liczba elementow musi byc dodatnia.')
            continue

        suma = 0

        for i in range(ile):
            liczba = float(input('Podaj liczbe: '))
            suma = suma + liczba

        srednia = suma / ile
        print('Srednia:', srednia)


            
            
        









