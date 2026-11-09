studenty = int(input('Podaj liczbe studentow: '))

punkty = []

for n in range(studenty):
    p = int(input(f'Punkty studenta {n+1}: '))
    punkty.append(p)

print('Punkty studentow:', punkty)

print('Srednia:', sum(punkty) / len(punkty))
print('Najwyzszy wynik:', max(punkty))
print('Najnizszy wynik:', min(punkty))
print('Wyniki rosnaco:', sorted(punkty))

zaliczenia = 0

for i in punkty:
    if p>=50:
        zaliczenia=+1

print('Liczba zaliczen:', zaliczenia)