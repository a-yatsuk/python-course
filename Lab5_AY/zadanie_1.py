import numpy as np

measurements = []

number = int(input("Please write the number of measurements: "))

for i in range(number):
    measurements.append(int(input(f'Please write the measurement {i+1}:  ')))


if not measurements:
    print('No measurements were given')

else:
    m = np.array(measurements)
    print(f"Measurements: {measurements}")
    print(f"Mean: {np.mean(m)}")
    print(f"Minimum: {np.min(m)}")
    print(f"Maximum: {np.max(m)}")
    print(f"Cleft: {np.max(m) - np.min(m)}")
