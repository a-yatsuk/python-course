cena = int(input('Podaj cene produktu: '))
rabat = int(input('Podaj rabat(%): '))

if cena >= 0 and 0<=rabat<=100:
        print(f'Cena początkowa: {cena}zł')
        kwota_rabatu = (cena/100)*rabat
        print(f'Kwota rabatu: {kwota_rabatu} zł')
        po_rabacie = cena - kwota_rabatu
        print(f'Cena po rabacie: {po_rabacie} zł') 
       


if rabat >= 20:
        print('Duża promocja! ')

else:
        print('Standarowa promocja')
