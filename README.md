Los códigos creados en este proyecto permiten observar la señal obtenida del sofware PHYSIONET, la cual es electroencefalografía (EEG), que en este caso mide por un método no invasivo los niveles de activación de distintas zonas del cerebro, evaluando  la actividad del cerebro. 

Se realizan distintas caracterizaciones de la señal, cálculos estadísticos y una ampliación de un segmento específico para un análisis más detallado y más preciso. 

El código carga una señal EMG desde un sofware llamado pyhsionet, donde se busca la parte de ¨data¨,  y se busca la señal a evdienciar que en este caso es EEG, este ejecuta distintos archivos, se debe buscar especificamente el .hea y .data del mismo nombre (ejemplo; EEG-1.hea y EEG-1.data), para posterior, importarla y visualizarla  en un programador llamado pyhton (spyder), que permitira hacer el cálculo de estadísticos importantes como la media, desviación estándar y coeficiente de variación, a su vez se obtiene el gráfico secuencial de la convolución .


Es importante mencionar que para correr el codigo y que funcione correctamente se deben descargar ciertas cosas, inicialmente en la consola de spyder se deben descargar ciertas librerías como; pip install numpy matplotlib wfdb scipy, estas soon para;

- import numpy as np: es para que permita correr cálculos númericos y arrays en caso de tenerlos.
- import matplotlib.pyplot as plt :permite visualizar los datos
- import wfdb ; esta va a leer y a su vez usar las señales fisiológicas que en este caso es una EEG para implementarlo en un formato estándar.
- Scipy ; es para la parte estadistica más avazada que incluye ;
              - from scipy.fftpack import fft; hace la transformada de                       fourier de una forma rápida , y se usa para analizar en                      este caso la señal eeg. 
            -  from scipy.signal import welch ; on esta se estima la 
               densidad espectral de potencia, también detecta patrones de 
               actividad cerebal, esto lo veremos más adelante




Posterior a esta verificación del programador que se va a implementar, se procederá a descargar la señal como se mencionó anteriormente, asegurandose que tengan el mismo nombre como ya se ejemplificó, y de esta forma se guarda en un archivo (por ejemplo con nombre; analisis_emg.py)que se encuentre en la misma carpeta de el script y  ejecuta el script de la siguiente forma;  python analisis_emg.py. Para continuar, se interpretan los resultados obtenidos de esto;


1. En primer lugar, se obtuvo un sistema y la señal para obtener lo siguiente;

      1.1. La convolución usando sumatorias  a mano, lo cual se evidencia               en....... con este sistema y señal incial  
      1.2. Se obtuvo la representación gráfica y secuencial a mano, esto                para identificar.........
      1.3. Se realizó el mismo procedimiento del item 1.1 pero esta vez                   usando python, lo que a su vez permite realizar una comparación.
      1.4. En este item, se obtuvo una representación gráfica y secuencial              en phyton, con el fin de..........

      
2. ⁠En segundo lugar, se tenían dos señales, donde se observó si tenian correlación, y a su vez se determinó la representación gráfica y secuencial, lo que se visualiza en el archivo .......

Es necesario comprender estos conceptos  de estadísticos descriptivos antes de continuar;
   - Los estadisticos descriptivos; se dividen en 

   
3.Por último, se realizó la descarga de la señal del software physionet. En github se evidencian los dos archivos del mismo: .dat y .hea, donde se realizó lo siguiente;

   3.1. Se caracterizó la señal en función del tiempo, donde a su vez se calcularon los estadisticos descriptivos, de lo cual podemos evidenciar que.....

   3.2. La señal en cuanto a la clasificación es;
   

   3.3. Aplicando la transformada de fourier de la señal, se graficó la transformada y la densidad espectral.....

3.4. Se analizaron los estadistícos descriptivos en función a la frecuencia, teniendo en cuenta que;

• Frecuencia media; indica el promedio que se obtiene al dividir la suma del total de los datos que se tengan entre el total de los mismos, de manera similar, esta proporciona un punto de equilibrio en la distribución de llos diferentes datos.

• Frecuencia mediana; este es el valor de la mitad de un conjunto de datos, en caso de haber un número total impar es el dato de la mitad, y si es par es el promedio de los valores centrales, y esta se usa cuando los datos se encuentran agrupados en intervalos.

• Desviación estándar ; esta permite medir la dispersión en el conjunto de datos que se este estudiando, y a su vez, se utiliza simultáneamente con la media para determinar los distintos intervalos estadísticos.

• Histograma: Este tipo de grafico, consiste en la representación de una variable cuantitativa por medio de barras, agrupando los datos, donde en el eje x se representan los intervalos de los datos y en el eje y evidencia la frecuencia de los datos en cierto intervalo, es la representación empirica de los datos observados en nuestro caso son las barras grises).


Con estos terminos claros, se comprende que respecto a los valores obtenidos, es posible analizar que....................
