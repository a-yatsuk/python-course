import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate grades
def oblicz_ocene(punkty):
    if punkty < 50:
        return 2.0
    elif punkty < 60:
        return 3.0
    elif punkty < 70:
        return 3.5
    elif punkty < 80:
        return 4.0
    elif punkty < 90:
        return 4.5
    else:
        return 5.0


# Lists
names = []
points = []

# Number of students
while True:
    number = input("Podaj liczbe studentow: ").strip()

    if number.isdigit() and int(number) >= 1:
        number = int(number)
        break
    else:
        print("Liczba studentow musi byc wieksza od 0!")


# Student information
for i in range(number):

    while True:
        name = input(f"Nazwisko studenta {i+1}: ").strip()

        if name != "":
            names.append(name)
            break
        else:
            print("Nazwisko nie moze byc puste!")

    while True:
        score = input("Punkty (0-100): ").strip()

        if score.isdigit() and 0 <= int(score) <= 100:
            points.append(int(score))
            break
        else:
            print("Punkty musza byc od 0 do 100!")


# Create DataFrame
df = pd.DataFrame({
    "Nazwisko": names,
    "Punkty": points
})

# Calculate grades
df["Ocena"] = df["Punkty"].apply(oblicz_ocene)

# Display table
print("\nWyniki egzaminu:")
print(df)

# Statistics
srednia = df["Ocena"].mean()
zaliczenia = (df["Ocena"] >= 3.0).sum()

print(f"\nSrednia ocen: {srednia}")
print(f"Liczba zaliczen: {zaliczenia}")

# Sort by points
posortowane = df.sort_values("Punkty", ascending=False)

print("\nPosortowane wyniki:")
print(posortowane)

# Bar chart
plt.bar(df["Nazwisko"], df["Ocena"])

plt.title("Wyniki egzaminu")
plt.xlabel("Student")
plt.ylabel("Ocena")
plt.ylim(0, 5.5)

plt.tight_layout()
plt.show()