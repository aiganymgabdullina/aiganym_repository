import pandas as pd
import numpy as np
#1 esep
file_path = 'catalog_products.xlsx'
df = pd.read_excel(file_path)
print("#1")
print(df.head())
print(f"\nФорма DataFrame: {df.shape}")
print(df.dtypes)
print(df.isnull().sum())

#2 esep
numeric_cols = df.select_dtypes(include=['number']).columns
for col in numeric_cols:
    df[col] = df[col].astype(float).fillna(df[col].mean())
text_cols = df.select_dtypes(include=['object', 'string']).columns
df = df.dropna(subset=text_cols)
print("#2")
print(f"Форма DataFrame после очистки: {df.shape}")
print(f"Общее количество пропусков: {df.isnull().sum().sum()}")

#3 esep
df['total_value'] = df['col_2'] * df['col_3']
df['log_price'] = np.log(df['col_2'])
df['double_stock'] = df['col_3'] * 2
print("#3")
print(df[['col_2', 'col_3', 'total_value', 'log_price', 'double_stock']].head())