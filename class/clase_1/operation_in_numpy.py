import numpy as np
print()

x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[6, 8, 9], [1, 2, 3]])
print(f"x = {x}")
print(f"y = {y}")

# Suma punto a punto
z = x + y
print(z)

# Resta punto a punto
z = x - y
print(z)

# Multiplicación punto a punto
# Las matrices deben ser del mismo tamaño y el resultado es una matriz del mismo tamaño
z = x * y
print(z)

# División punto a punto
# Las matrices deben ser del mismo tamaño y el resultado es una matriz del mismo tamaño
z = x / y
print(z)


# Producto punto entre arreglos
x = np.array([1, 2, 3])
y = np.array([6, 8, 9])
print(f"x = {x}")
print(f"y = {y}")

z = np.dot(x, y)
print(z)


# Producto punto entre matrices
x = np.array([[3, 2, 3], [3, 2, 3]])
y = np.array([[4, 5], [6, 7], [8, 9]])
print(f"x = {x}")
print(f"y = {y}")

z = np.dot(x, y)
print(z)

# Producto punto entre matrices (Simplificado)
x = np.array([[3, 2, 3], [3, 2, 3]])
y = np.array([[4, 5], [6, 7], [8, 9]])
print(f"x = {x}")
print(f"y = {y}")

z = x @ y
print(z)


# Seno a cada componente
print(f"Seno de x = {np.sin(x)}")


renodeo_arriba = np.ceil(np.sin(x))
print(f"Redondeo hacia arriba {renodeo_arriba}")

renodeo_abajo = np.floor(np.sin(x))
print(f"Redondeo hacia abajo {renodeo_abajo}")

renodeo = np.round(np.sin(x), 2)
print(f"Redondeo {renodeo}")

# Comparación entre arreglos
x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[6, 8, 9], [1, 2, 3]])
z = x > y
print(f"Comparación entre x > y = {z}")
print(f"Tipo de dato de z = {z.dtype}")

print(f"Promedio de los elementos de a una matriz {np.mean(x)}")
print(f"Minimo de los elementos de a una matriz {np.min(x)}")
print(f"Maximo de los elementos de a una matriz {np.max(x)}")
print(f"Moda de los elementos de a una matriz {np.median(x)}")

# Concatenación entre matrices
z = np.concatenate((x, y), axis=0)
print(f"Concateción de X y Y = {z}")
