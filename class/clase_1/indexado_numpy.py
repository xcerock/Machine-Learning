import numpy as np
print()

x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[6, 8, 9], [1, 2, 3]])

print(f"Primer elemento de la primera fila {x[0, 0]} X")
print(f"Ultimo elemento de la ultima  fila {x[-1, -1]} X")
print(f"Primera fila del vector x[0, :] {x[0, :]}")
print(
    f"El primer elemento desde el primer elemento hasta el penultimo x[0, 0:2] {x[0, 0:2]}")

a = np.array([1, 2, 3, 4, 5, 6])
print(f"a = {a}")

# Reordenar el orden una vector como matriz
print(f"Reshape(a) = \n {a.reshape(2, 3)}")


a = np.array([[1, 2, 3, 4], [5, 5, 5, 6], [5, 5, 5, 6]])
print(f"a = {a}")

# Reordenar el orden una matriz a otra matriz
print(f"Reshape(a) = \n {a.reshape(6, 2)}")

# Broadcasting
print(f"a + 1 = {a + 1}")

b = np.array([1, 0, -1, 2])
print(f"Matriz b = {b}")

print(f"a + b = {a + b}")

# Calcular la descomposición de Cholesky
A = np.array([[1, 2, 3], [2, 5, 6], [3, 6, 10]])
print(f"A = {A}")
L = np.linalg.cholesky(A)
print(f"L = {L}")

Q, R = np.linalg.qr(A)
print(f"Q = {Q}")
print(f"R = {R}")

w, v = np.linalg.eig(A)
print(f"w = {w}")
print(f"v = {v}")

b = np.array([1, 2, 3])
x = np.linalg.solve(A, b)
print(f"x = {x}")

Ainv = np.linalg.inv(A)
print(f"Ainv = {Ainv}")


detA = np.linalg.det(A)
print(f"Determinante de A = {detA}")

# Generar aleatorios entre 0 y 1
r = np.random.rand()
print(f"r = {r}")

# Para normalizar datos
r = np.random.randn(4) * 2 + 10
print(f"r = {r}")


A = np.array([[1, 2, 3], [2, 5, 6], [3, 6, 10], [3, 6, 10]], dtype=np.float64)
suma_filas = np.sum(A, axis=1)
print(f"Suma de filas = {suma_filas}")

suma_columnas = np.sum(A, axis=0)
print(f"Suma de columnas = {suma_columnas}")
