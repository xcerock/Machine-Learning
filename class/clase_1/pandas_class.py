import numpy as np
import pandas as pd
print()

data = [1, 2, 3, 4, 5]
index = ["a", "b", "c", "d", "e"]
serie = pd.Series(data, index=index)
print(serie)
print(f"serie['c'] = {serie['c']}")

serie_2 = serie * 2
print(serie_2)

serie_bool = serie > 2
serie_3 = serie[serie_bool]
print(serie_bool)
print(serie_3)

data = {
    'Columna1': [1, 2, 3, 4, 5],
    'Columna2': ['a', 'b', 'c', 'd', 'e'],
    'Columna3': [1.1, 2.2, 3.3, 4.4, 5.5]
}

df = pd.DataFrame(data)
print(df)
