tyg_kwota = float(input('Prosze podac  kwote odkladanej co tydien '))
tygodznie = int(input('Prosze podac liczbe tygodni'))
oszczednosci = 0

for i in range(1, tygodznie+1):
    oszczednosci = tyg_kwota + oszczednosci
    print(f"Tydzień {i}: {oszczednosci:.2f} zł")
    print(f"Łącznie zaoszczędzono: {oszczednosci:.2f} zł")



