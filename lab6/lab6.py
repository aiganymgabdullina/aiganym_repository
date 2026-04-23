#1 esep
import pandas as pd
df = pd.read_excel('catalog_products.xlsx')
print("#1")
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
print("#2")
print(df[['col_2', 'col_3']].head())

#3 esep
import numpy as np
df['total_value'] = df['col_2'] * df['col_3']
df['double_stock'] = df['col_5'] * 2
df['log_price'] = np.log(df['col_2'])
print("#3")
print(df[['total_value', 'double_stock', 'log_price']].head())

#4 esep
import pandas as pd
file_name = 'catalog_products.xlsx'
df = pd.read_excel(file_name)
df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')
mask = (df['col_2'] > 500) & (df['col_7']== "Electronics")
electronics_expensive = df.loc[mask, ['col_2', 'col_7']].copy()
print("#4")
print(electronics_expensive.head())

#5 esep
category_analysis = df.groupby('col_7').agg(
    mean_price=('col_2', 'mean'),
    max_price=('col_2', 'max'),
    total_quantity=('col_3', 'sum')
).reset_index()
category_analysis = category_analysis.rename(columns={'col_7': 'category'})
print("#5")
print(category_analysis)

#6 esep
target_cols = [f'col_{i}' for i in range(2, 12)]
subset = df[target_cols].copy()
for col in target_cols:
    subset[col] = pd.to_numeric(subset[col], errors='coerce')
stats = subset.agg(['mean', 'median', 'std']).T
stats_df = stats.reset_index().rename(columns={'index': 'column'})
print("#6")
print(stats_df)

#7 esep
df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')
mean_price = df['col_2'].mean()
std_price = df['col_2'].std()
threshold = mean_price + 3 * std_price
anomalies = df[df['col_2'] > threshold].copy()
print("#7")
print(threshold)
print(anomalies.head())

#8 esep
target_cols = [f'col_{i}' for i in range(2, 12)]
subset = df[target_cols].copy()
for col in target_cols:
    subset[col] = pd.to_numeric(subset[col], errors='coerce')
correlation_matrix = subset.corr()
print("#8")
print(correlation_matrix.iloc[:3, :3].round(2))

#9 esep
import pandas as pd
import matplotlib.pyplot as plt
df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')
plt.figure(figsize=(10, 6))
plt.hist(df['col_2'].dropna(), bins=50, color='skyblue', edgecolor='black')
plt.title('Распределение цен товаров (col_2)')
plt.xlabel('Цена товаров')
plt.ylabel('Количество товаров')
plt.grid(axis='y', alpha=0.75)
plt.show()