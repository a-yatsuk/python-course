import numpy as np

c = []

# Quantity of products
while True:
    number = input("Please write the quantity of products: ").strip()

    if number.isdigit() and int(number) > 0:
        number = int(number)
        break
    else:
        print("Please enter a positive number!")


while True:
    discount = input("Please write the discount (%): ").strip()

    if discount.isdigit() and 0 <= int(discount) <= 100:
        discount = int(discount)
        break
    else:
        print("Please enter a discount between 0 and 100!")

for i in range(number):
    while True:
        price = input(f"Please write the price {i+1}: ").strip()

        if price.isdigit():
            c.append(int(price))
            break
        else:
            print("Please enter a valid non-negative price!")


prices = np.array(c)

new_prices = np.round(prices * (1 - discount / 100), 2)


print(f"Original prices: {prices}")
print(f"New prices: {new_prices}")
print(f"Sum before discount: {np.sum(prices)}")
print(f"Sum after discount: {np.sum(new_prices)}")
print(f"Prices above 100 $: {new_prices[new_prices > 100]}")