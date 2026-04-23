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

#2 esep
df = pd.read_excel('catalog_products.xlsx')
cols_to_fix = df.columns[1:]
for col in cols_to_fix:
    df[col] = pd.to_numeric(df[col], errors='coerce').astype(float)
    df[col] = df[col].fillna(df[col].mean())
df[cols_to_fix].dtypes.head()
df[cols_to_fix].isnull().sum().head()
print(df[['col_2', 'col_3']].head())