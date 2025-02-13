import wfdb
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from scipy.signal import welch

# Ruta de los archivos
hea_file = 'slp01a'
dat_file = 'slp01a'

# Leer el registro
record = wfdb.rdrecord(hea_file.replace('.hea', ''))

# Extraer la señal
signal = record.p_signal[:, 0]  # Selecciona el primer canal si hay más de uno
fs = record.fs  # Frecuencia de muestreo

# Caracterización de la señal en función del tiempo
media = np.mean(signal)
mediana = np.median(signal)
desviacion = np.std(signal)
min_valor = np.min(signal)
max_valor = np.max(signal)

# Mostrar estadísticos descriptivos
print("Características de la señal en el tiempo:")
print(f"Frecuencia de muestreo: {fs} Hz")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Desviación estándar: {desviacion}")
print(f"Valor mínimo: {min_valor}")
print(f"Valor máximo: {max_valor}")

# Definir el fragmento ampliado
inicio = 15000  
fin = 30000
segmento = signal[inicio:fin]

# Graficar la señal completa
plt.figure(figsize=(12, 5))
plt.plot(signal, label="Señal completa", color='b')
plt.title('Señal EEG completa')
plt.xlabel('Tiempo(s)')
plt.ylabel('Voltaje [mV]')
plt.legend()
plt.grid()
plt.show()

# Graficar el segmento ampliado
plt.figure(figsize=(12, 5))
plt.plot(range(inicio, fin), segmento, label="Sección ampliado", color='r')
plt.title('Sección ampliado de la señal EEG')
plt.xlabel('Tiempo(s)')
plt.ylabel('Voltaje [mV]')
plt.legend()
plt.grid()
plt.show()

# Aplicar la Transformada de Fourier
N = len(segmento)
frecuencias = np.fft.fftfreq(N, d=1/fs)  # Eje de frecuencias
transformada = np.abs(fft(segmento)) / N  # Normalización

# Graficar la Transformada de Fourier corregida
plt.figure(figsize=(12, 5))
plt.plot(frecuencias[:N//2], transformada[:N//2], color='g')
plt.title("Transformada de Fourier del fragmento de señal EEG")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud normalizada")
plt.grid()
plt.show()

# Densidad espectral de potencia (PSD) con mejor ventana
frecuencias_psd, psd = welch(segmento, fs, nperseg=2048)

# Graficar la densidad espectral de potencia corregida
plt.figure(figsize=(12, 5))
plt.semilogy(frecuencias_psd, psd, color='m')
plt.title("Densidad espectral de potencia del fragmento de señal EEG")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Densidad espectral")
plt.grid()
plt.show()

# Graficar histograma de frecuencias
plt.figure(figsize=(12, 5))
plt.hist(frecuencias_psd, bins=50, weights=psd, color='c', alpha=0.7)
plt.title("Histograma de frecuencias de la señal EEG")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Frecuencia relativa")
plt.grid()
plt.show()

# Aplicar la Transformada de Fourier para la señal completa
N = len(signal)
frecuencias = np.fft.fftfreq(N, d=1/fs)[:N//2]  # Eje de frecuencias (solo parte positiva)
transformada = np.abs(fft(signal))[:N//2]  # Magnitud de la FFT (solo parte positiva)

# Cálculo de estadísticos en el dominio de la frecuencia
frecuencia_media = np.sum(frecuencias * transformada) / np.sum(transformada)
frecuencia_mediana = frecuencias[np.argmax(np.cumsum(transformada) >= np.sum(transformada) / 2)]
desviacion_frec = np.sqrt(np.sum(transformada * (frecuencias - frecuencia_media) ** 2) / np.sum(transformada))

# Mostrar estadísticos en frecuencia
print("\nCaracterísticas de la señal en frecuencia:")
print(f"Frecuencia media: {frecuencia_media:.2f} Hz")
print(f"Frecuencia mediana: {frecuencia_mediana:.2f} Hz")
print(f"Desviación estándar en frecuencia: {desviacion_frec:.2f} Hz")
print(f"Frecuencia mínima: {np.min(frecuencias):.2f} Hz")
print(f"Frecuencia máxima: {np.max(frecuencias):.2f} Hz")
