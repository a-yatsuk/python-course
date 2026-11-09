import matplotlib.pyplot as plt

surnames = []
points = []
grades = []

number = int(input("Enter the number of students: "))

for i in range(number):
    surname = input(f"Student {i + 1} surname: ")
    score = int(input("Points: "))

    if score < 50:
        grade = 2.0
    elif score < 60:
        grade = 3.0
    elif score < 70:
        grade = 3.5
    elif score < 80:
        grade = 4.0
    elif score < 90:
        grade = 4.5
    else:
        grade = 5.0

    surnames.append(surname)
    points.append(score)
    grades.append(grade)

print("\n===== RESULTS =====")

for surname, grade in zip(surnames, grades):
    print(f"{surname} - {grade}")

average = sum(grades) / len(grades)
passed = sum(1 for grade in grades if grade >= 3.0)

print(f"Average grade: {average}")
print(f"Number of students who passed: {passed}")

print("Generating chart...")

plt.bar(surnames, grades)
plt.title("Student Exam Grades")
plt.xlabel("Students")
plt.ylabel("Grades")
plt.ylim(0, 5.5)
plt.show()