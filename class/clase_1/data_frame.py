import numpy as np
import pandas as pd

data = {
    'Columna1': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    'Columna2': ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e'],
    'Columna3': [1.1, 2.2, 3.3, 4.4, 5.5, 1.1, 2.2, 3.3, 4.4, 5.5]
}

df = pd.DataFrame(data)
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())

print(df["Columna1"])

arreglo = np.array([
    [1, "a", 1.1],
    [2, 'b', 2.2],
    [3, 'c', 3.3],
    [4, 'd', 4.4],
    [5, 'e', 5.5]
])
columnas = ["Columna1", "Columna2", "Columna3"]
df = pd.DataFrame(arreglo, columns=columnas)
print(df)

df.dropna(inplace=True)
df.fillna(0, inplace=True)
df.interpolate(inplace=True)

grupo = df.groupby('Columna1')
print(grupo['Columna2'].mean())
