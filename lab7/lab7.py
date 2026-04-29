import pandas as pd
#1 esep
file_path = 'catalog_products.xlsx'
df = pd.read_excel(file_path)
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
print(f"Форма DataFrame после очистки: {df.shape}")
print(f"Общее количество пропусков: {df.isnull().sum().sum()}")