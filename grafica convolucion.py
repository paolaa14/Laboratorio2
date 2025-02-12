import numpy as np
import matplotlib.pyplot as plt


# Señales dadas en la imagen
x_n = [5, 6, 0, 0, 5, 0, 1]
h_n = [1, 0, 1, 3, 0, 9, 7, 6, 2, 0]

# Convolución de las señales
y_n = np.convolve(x_n, h_n)

# Mostrar la ecuación resultante
ecuacion = "y(n) = " + " + ".join(f"{y_n[i]}x^{i}" for i in range(len(y_n)))
print(ecuacion)


# Señales de entrada
x = np.array([5, 6, 0, 0, 5, 0, 1])
h = np.array([1, 0, 1, 3, 0, 9, 7, 6, 2, 0])

# Cálculo de la convolución
y = np.convolve(x, h)

# Configuración de la figura
plt.figure(figsize=(8, 5))

# Gráfica de la convolución
plt.stem(range(len(y)), y, basefmt=" ")

plt.xlabel('n')
plt.ylabel('y(n)')
plt.title('Gráfica de la convolución y(n)')
plt.grid()

plt.show()
