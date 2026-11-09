tem = int(input('Prosze wskazac aktualna temperature: '))
obecnosc = input('Czy ktos jest obecny w domu? ').strip().lower()
okno = input('Czy pkno jest otwarte? ').strip().lower()

if okno == 'tak':
    print('Ogrzewanie WYLACZONE')
    print('Powod: Okno jest otwarte')

elif okno == 'nie' and obecnosc == 'tak' and tem < 20:
    print('Ogrzewanie WLACZONE')
    print('Powod: Temperatura ponizej 20°C')

elif okno == 'nie' and obecnosc == 'nie' and tem < 16:
    print('Ogrzewanie WLACZONE')
    print('Powod: Temperatura ponizej 16°C, nikogo nie ma w domu')

else:
    print('Ogrzewanie WYLACZONE')
    print('Powod: Temperatura nie wymaga ogrzewania')