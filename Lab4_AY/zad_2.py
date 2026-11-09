products = []
prices = []

number = int(input(f"Please write the number of products: "))

for n in range(number):
    products.append(input('Please write the product: '))
    prices.append(int(input('Please write the price: ')))


for number, product in enumerate(products, start =1):
    print(number, product)


for product, price in zip(products, prices):
    print(product, price)

print(f'Sum of products: {sum(prices)}')
print(f"The most expensive product: {[f'{product} - {price}' for product, price in zip(products, prices) if price == max(prices)]}")