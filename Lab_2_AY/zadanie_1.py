zakupy = []

liczba = int(input("Ile produktow chcesz dodac? "))

for i in range(liczba):
    produkt = input(f"Produkt {i + 1}: ").strip()
    zakupy.append(produkt)

print("Lista:", zakupy)
print("Liczba produktow:", len(zakupy))

usun = input("Produkt do usuniecia: ").strip().lower()

for produkt in zakupy:
    if produkt.lower() == usun:
        zakupy.remove(produkt)
        break
else:
    print("Nie ma takiego produktu na liscie.")

print("Nowa lista:", zakupy)