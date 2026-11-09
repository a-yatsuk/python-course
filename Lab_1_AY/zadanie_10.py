students = int(input('Podaj liczbe studentow: '))
zaliczyli = 0

for s in range(1, students + 1):
    nazwisko = input(f'Podaj nazwisko studenta {s}: ')
    punkty = int(input('Podaj liczbe punktow: '))

    if punkty < 0 or punkty > 100:
        print('Nieprawidlowa liczba punktow')
        continue
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

    print(f'{nazwisko} - {punkty} pkt - ocena {ocena:.1f}')

    if ocena >= 3.0:
        zaliczyli += 1

print(f'Studenci ktorzy zaliczyli: {zaliczyli}')



    