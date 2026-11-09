poczatek = int (input('Prosze podac poczatekzakresu : '))
koniec = int(input('Prosze podac koniec zakresu: '))
parzyste = 0

for i in range(poczatek, koniec+1 ):
    if i%2 ==0:
        print(f"{i} - Parzysta liczba")
        parzyste +=1
    else:
        print(f"{i} - Nieparzysta liczba")

print(f"Liczba liczb parzystych: {parzyste}")


