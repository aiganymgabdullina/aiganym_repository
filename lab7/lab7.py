import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
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

#4 esep
sns.set_theme(style="whitegrid")


plt.figure(figsize=(10, 6))
sns.histplot(df['col_2'], kde=True, color='skyblue')
plt.title('Распределение цен товаров')
plt.xlabel('Цена (col_2)')
plt.ylabel('Частота')
plt.show()


plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='col_3', y='col_2', alpha=0.6)
plt.title('Связь цены и количества товара')
plt.xlabel('Количество (col_3)')
plt.ylabel('Цена (col_2)')
plt.show()


plt.figure(figsize=(12, 8))
sns.boxplot(data=df, x='col_7', y='col_2')
plt.title('Разброс цен по категориям')
plt.xlabel('Категория (col_7)')
plt.ylabel('Цена (col_2)')
plt.tight_layout()
plt.show()

#5 esep
mean_price = df['col_2'].mean()
std_price = df['col_2'].std()
lower_bound = mean_price - 3 * std_price
upper_bound = mean_price + 3 * std_price
anomalies = df[(df['col_2'] > upper_bound) | (df['col_2'] < lower_bound)]
df_cleaned = df[(df['col_2'] <= upper_bound) & (df['col_2'] >= lower_bound)]
print("#5")
print(anomalies[['col_2', 'col_7']].head())

#6 esep
df_final = pd.get_dummies(df_cleaned, columns=['col_7'], drop_first=True).select_dtypes(exclude=['object'])
print("#6")
print(all(df_final.dtypes.apply(lambda x: pd.api.types.is_numeric_dtype(x))))

#7 esep
y = df_final['col_2']
X = df_final.drop(columns=['col_2'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("#7")
print(all(X.dtypes.apply(lambda x: pd.api.types.is_numeric_dtype(x))))

#8 esep
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
print("#8")
print(f"Средняя абсолютная ошибка (MAE): {mae:.2f}")
print(f"Среднеквадратичная ошибка (MSE): {mse:.2f}")

#9 esep
model_improved = LinearRegression()
model_improved.fit(X_train, y_train)
y_pred_improved = model_improved.predict(X_test)
mae_improved = mean_absolute_error(y_test, y_pred_improved)
mse_improved = mean_squared_error(y_test, y_pred_improved)
print("#9")
print(f"MAE (Базовая модель): {mae:.2f}  ->  MAE (Улучшенная): {mae_improved:.2f}")
print(f"MSE (Базовая модель): {mse:.2f}  ->  MSE (Улучшенная): {mse_improved:.2f}")
improvement = ((mae - mae_improved) / mae) * 100
print(f"\nТочность предсказания улучшилась на: {improvement:.2f}%")

#10 esep
plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_pred_improved, alpha=0.5, color='teal', label='Предсказания')
min_val = min(y_test.min(), y_pred_improved.min())
max_val = max(y_test.max(), y_pred_improved.max())
plt.plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--', lw=2, label='Идеальное предсказание')
plt.title('Сравнение истинных цен и предсказаний модели')
plt.xlabel('Истинная цена (y_test)')
plt.ylabel('Предсказанная цена (y_pred)')
plt.legend()
plt.grid(True)
plt.show()

#11 esep
features_to_scale = ['col_3', 'total_value', 'double_stock', 'log_price']
scaler = StandardScaler()
X_train[features_to_scale] = scaler.fit_transform(X_train[features_to_scale])
X_test[features_to_scale] = scaler.transform(X_test[features_to_scale])
print("#11")
print(f"Среднее после StandardScaler: {X_train[features_to_scale].mean().mean():.2f}")
print(f"Стандартное отклонение: {X_train[features_to_scale].std().mean():.2f}")