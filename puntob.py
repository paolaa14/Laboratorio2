import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
Fs = 1 / 1.25e-3  # Frecuencia de muestreo (1 / Ts)
n = np.arange(0, 9, 1)  # Vector de tiempo discreto
Ts = 1.25e-3  # Período de muestreo

# Señales dadas
x1 = np.cos(2 * np.pi * 100 * n * Ts)  # x1[nTs] = cos(2π100nTs)
x2 = np.sin(2 * np.pi * 100 * n * Ts)  # x2[nTs] = sin(2π100nTs)

# Correlación entre las señales
corr_x1_x2 = np.correlate(x1, x2, mode='full')

# Representación gráfica
plt.figure(figsize=(12, 6))

# Gráfica de las señales x1 y x2
plt.subplot(2, 1, 1)
plt.stem(n, x1, linefmt='b-', markerfmt='bo', basefmt='r-', label="x1[n]")
plt.stem(n, x2, linefmt='g-', markerfmt='go', basefmt='r-', label="x2[n]")
plt.xlabel("n")
plt.ylabel("Amplitud")
plt.title("Señales x1[n] y x2[n]")
plt.legend()
plt.grid()

# Gráfica de la correlación
plt.subplot(2, 1, 2)
lags = np.arange(-len(n) + 1, len(n))  # Definir los lags
plt.stem(lags, corr_x1_x2, linefmt='m-', markerfmt='mo', basefmt='r-')
plt.xlabel("Desplazamiento (lag)")
plt.ylabel("Correlación")
plt.title("Correlación entre x1[n] y x2[n]")
plt.grid()

plt.tight_layout()
plt.show()

# Representación secuencial
print("Secuencia de correlación:", corr_x1_x2.tolist())

