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

# Crear las figuras separadas
plt.figure(figsize=(8, 4))
plt.stem(range(len(x_n)), x_n, basefmt=" ", linefmt='b-', markerfmt='bo')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Señal x(n)')
plt.grid()
plt.show()

plt.figure(figsize=(8, 4))
plt.stem(range(len(h_n)), h_n, basefmt=" ", linefmt='r-', markerfmt='ro')
plt.xlabel('n')
plt.ylabel('h(n)')
plt.title('Señal h(n)')
plt.grid()
plt.show()

plt.figure(figsize=(10, 4))
plt.stem(range(len(y_n)), y_n, basefmt=" ", linefmt='g-', markerfmt='go')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.title('Gráfica de la convolución y(n)')
plt.grid()
plt.show()
