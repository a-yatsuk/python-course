import pandas as pd

products = ['Audi', 'BMW', 'Ferrari']
prices = [50000, 40000, 250000]
available = [4, 9, 2]

df = pd.DataFrame({
    "Products": products,
    "Prices": prices,
    "Available": available
})

df['Value'] = df['Prices'] * df['Available']

print(df)

print(df[df['Prices'] > 100])

print(f"Sum: {df['Value'].sum()}")
print(f"Mean: {df['Prices'].mean():.2f}")