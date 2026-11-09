wiek = int(input('Prosze wpisac swoj wiek: '))

if 13 <= wiek < 18:
    zgoda = input("Czy posiadasz zgode opiekuna (tak/nie): ").strip().lower()
else:
    zgoda = 'nie'


dokument = input("Czy posiadasz dokument tozsamosci (tak/nie): ").strip().lower()


if dokument == "tak" and (wiek >= 18 or (wiek >= 13 and zgoda == "tak")):
    print('Wypozyczenie mozliwe')

else:
    print('Wypozyczenie niemozliwe')
