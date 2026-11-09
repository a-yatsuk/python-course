punkty = int(input("Podaj liczbę punktów: "))

if punkty < 0 or punkty > 100:
    print("Błędna liczba punktów")
elif punkty < 50:
    ocena = 2.0
elif punkty < 60:
    ocena = 3.0
elif punkty < 70:
    ocena = 3.5
elif punkty < 80:
    ocena = 4.0
elif punkty < 90:
    ocena = 4.5
else:
    ocena = 5.0

if 0 <= punkty <= 100:
    print(f"Liczba punktów: {punkty}")
    print(f"Uzyskana ocena: {ocena:.1f}")