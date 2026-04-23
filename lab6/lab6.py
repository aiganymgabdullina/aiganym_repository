#1 esep
import pandas as pd
df = pd.read_excel('catalog_products.xlsx')
print(f"Форма DataFrame: {df.shape}")
print("\nТипы данных:")
print(df.dtypes)
print("\nПропуски:")
print(df.isnull().sum())
print("\nПервые 5 строк:")
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(df.head())