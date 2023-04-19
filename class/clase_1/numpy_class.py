import numpy as np

print()

# Imprimir versión actual de numpy
print(np.__version__)

# Arreglo unidimensional
example = np.array([1, 2, 3, 4])

print(example)

# Arreglo tridimensional
example = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])

print(example)

# Dimensiones
print(example.ndim)

# Número de elementos
print(example.size)

# Llena un vector en 0
example = np.zeros(10)

print(example)

# Llena un vector en 1
example = np.ones(10)

print(example)

# Llena una matriz en 0
example = np.zeros((2, 3))

print(example)

# Llena una matriz en 0 usando enteros (Por defecto es dobules)
example = np.zeros((2, 3), dtype=int)

print(example)
