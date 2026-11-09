measurements = []

number = int(input('Please write the number of measurements: '))

for n in range(number):
    measurements.append(int(input(f" Pomiar {n+1}")))


print(f" First measurement: {measurements[0]}")
print(f"Three first measurements: {measurements[0:2]}")
print(f"Every second measurement:{measurements[::2]} ")
print(f' Reversed list: {measurements[::-1]}')
print(f"Original list: {measurements}")
copy = measurements.copy()
copy[0]=0
print(f'The copy after change:{copy}')





