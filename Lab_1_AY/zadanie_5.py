godziny = int(input('Podaj godziny parkowania(h): '))
print(f"Czas postoju(h): {godziny}")


if godziny <=0:
    print('Wpisane dane sa nieprawidlowe')
elif 0<godziny<=1:
    print('Oplata za parking wynosi 5 zl')
elif 1<godziny<=3:
    print('Oplata za parking wynosi 12 zl')
elif 3<godziny<=6:
    print('Oplata za parking wynosi 20 zl')
elif godziny>6:
    print('Oplata za parking wynosi 30 zl')

    