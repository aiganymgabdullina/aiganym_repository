import pandas as pd
#1 esep
file_path = 'catalog_products.xlsx'
df = pd.read_excel(file_path)
print(df.head())
print(f"\nФорма DataFrame: {df.shape}")
print(df.dtypes)
print(df.isnull().sum())