measurements = []
threshold = 50

number = int(input("Enter the number of measurements: "))

for i in range(number):
    measurement = int(input(f"Measurement {i + 1}: "))
    measurements.append(measurement)

alarm_measurements = [x for x in measurements if x > threshold]

doubled_measurements = [x * 2 for x in measurements]

alarm = any(x > threshold for x in measurements)

all_correct = all(x <= threshold for x in measurements)

print(f"Alarm measurements: {alarm_measurements}")
print(f"Doubled measurements: {doubled_measurements}")
print(f"Did an alarm occur? {'Yes' if alarm else 'No'}")
print(f"Are all measurements correct? {'Yes' if all_correct else 'No'}")


