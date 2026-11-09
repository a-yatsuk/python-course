napoje = ["Woda", "Sok", "Cola"]
ceny = [3, 5, 6]
suma = 0

while True:
    print("1. Woda - 3 zl")
    print("2. Sok - 5 zl")
    print("3. Cola - 6 zl")
    print("0. Zakoncz")

    wybor = int(input("Wybierz opcje: "))

    if wybor == 0:
        break
    elif 1 <= wybor <= 3:
        indeks = wybor - 1
        print(f"Wybrano: {napoje[indeks]}, cena: {ceny[indeks]} zl")
        suma += ceny[indeks]
    else:
        print("Nieprawidlowa opcja")

print(f"Lacznie do zaplaty: {suma} zl")