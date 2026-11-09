cena = int(input('Podaj cene produktu '))
ilosc = int(input('Podaj liczbe sztuk '))
koszt_dostawy = 12

calkowity_koszt = cena*ilosc
print(f"Wartość produktów :{calkowity_koszt}")

if calkowity_koszt>=100:
    print('Do zapłaty {calkowity_koszt} zł, dostawa darmowa')
else:
    print(f"Do zapłaty z dostawą {calkowity_koszt + koszt_dostawy}")