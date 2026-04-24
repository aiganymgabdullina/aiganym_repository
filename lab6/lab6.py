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

#14 esep
final_cols = ['col_1', 'col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_7',
              'total_value', 'double_stock', 'log_price']
df[final_cols].to_excel('catalog_analysis.xlsx', index=False)

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
plt.title('Распределение цен товаров ')
plt.xlabel('Цена товаров')
plt.ylabel('Количество товаров')
plt.grid(axis='y', alpha=0.75)
plt.show()

#10 esep
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_excel("catalog_products.xlsx")
df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')
df['col_3'] = pd.to_numeric(df['col_3'], errors='coerce')
plt.figure(figsize=(10, 6))
sns.regplot(x='col_2', y='col_3', data=df,
            scatter_kws={'alpha':0.5, 'color':'blue'},
            line_kws={'color':'red'})
plt.title('Взаимосвязь цены и количества товара на складе')
plt.xlabel('Цена ')
plt.ylabel('Количество на складе')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

#11 esep
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')
plt.figure(figsize=(12, 6))
sns.boxplot(x='col_7', y='col_2', data=df)
plt.title('Распределение цен по категориям')
plt.xlabel('Категория')
plt.ylabel('Цена ')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#12 esep
df_12 = df[['col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_7']]
sns.pairplot(df_12, hue = "col_7")
plt.show()


#13 esep
df_13 = df[[f'col_{i}' for i in range(2, 12)]].apply(pd.to_numeric, errors='coerce')
corr_matrix = df_13.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Тепловая карта корреляции характеристик товаров (col_2-col_11)', fontsize=15)
plt.show()

#14 esep
#3 eseppen connected

#15 esep
df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')
df['col_3'] = pd.to_numeric(df['col_3'], errors='coerce')
if 'log_price' not in df.columns:
    import numpy as np
    df['log_price'] = np.log1p(df['col_2'])
category_summary = df.groupby('col_7').agg({
    'col_1': 'count',
    'col_2': 'mean',
    'col_3': 'sum',
    'log_price': 'mean'
})
category_summary.columns = ['count', 'mean_price', 'total_quantity', 'mean_log_price']
print("#15")
print(category_summary.head())
category_summary.to_excel('final_summary.xlsx')

#16 esep
import pandas as pd
df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')
idx = df.groupby('col_7')['col_2'].idxmax()
most_expensive = df.loc[idx, ['col_1', 'col_2', 'col_7']]
print("#16")
print(most_expensive)

#17 esep
df['total_value'] = pd.to_numeric(df['col_2'], errors='coerce') * pd.to_numeric(df['col_3'], errors='coerce')
top_10_expensive = df.sort_values(by='total_value', ascending=False).head(10)
result = top_10_expensive[['col_1', 'col_2', 'col_3', 'total_value']]
print("#17")
print(result)

#18 esep
bins = [0, 50, 200, 500, 1000, float('inf')]
labels = ['0-50', '50-200', '200-500', '500-1000', '>1000']
df['price_range'] = pd.cut(pd.to_numeric(df['col_2'], errors='coerce'), bins=bins, labels=labels)
price_dist = df['price_range'].value_counts().reindex(labels).reset_index()
price_dist.columns = ['price_range', 'count']
sns.barplot(data=price_dist, x='price_range', y='count', hue='price_range', palette='viridis', legend=False)
plt.title('Распределение товаров по ценам')
plt.show()
print("#18")
print(price_dist)

#19 esep
df['total_value'] = pd.to_numeric(df['col_2'], errors='coerce') * pd.to_numeric(df['col_3'], errors='coerce')
cat_value = df.groupby('col_7')['total_value'].sum().reset_index()
cat_value.columns = ['category', 'total_stock_value']
max_cat = cat_value.loc[cat_value['total_stock_value'].idxmax()]
print(f"Категория с макс. капиталом: {max_cat['category']} ({max_cat['total_stock_value']})")
sns.barplot(data=cat_value, x='category', y='total_stock_value', hue='category', palette='magma', legend=False)
plt.title('Суммарная стоимость товаров на складе по категориям')
plt.xticks(rotation=45)
plt.show()
print("#19")
print(cat_value)

#20 esep
cat_stats = df.groupby('col_7').agg({
    'col_2': 'mean',
    'col_3': 'mean'
}).reset_index()
cat_stats.columns = ['category', 'mean_price', 'mean_quantity']
plt.figure(figsize=(10, 6))
sns.scatterplot(data=cat_stats, x='mean_price', y='mean_quantity', hue='category', s=200)
plt.title('Средняя цена vs Средний запас по категориям')
plt.xlabel('Средняя цена')
plt.ylabel('Средний запас')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
print("#20")
print(cat_stats)

#21 esep
price_variation = df.groupby('col_7')['col_2'].std().reset_index()
price_variation.columns = ['category', 'std_price']
sns.barplot(data=price_variation.sort_values('std_price', ascending=False),
            x='std_price', y='category', hue='category', palette='magma', legend=False)
plt.title('Разброс цен (стандартное отклонение) по категориям')
plt.xlabel('Стандартное отклонение цены')
plt.ylabel('Категория')
plt.show()
print("#20")
print(price_variation)

#22 esep
out_of_stock = df[df['col_3'] == 0]
result = out_of_stock[['col_1', 'col_7', 'col_2']].head(10)
print("#22")
print(result)