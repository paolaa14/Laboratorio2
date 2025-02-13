En este proyecto se realizan distintos cálculos en un determinado sistema, al cual se le hallará la señal resultante de la convolución implementando sumatorias, posterior se encontrará la representación gráfica y secuencial del sistema mencionado anteriormente, todo esto se hará a mano con el fin de fortalecer las bases para conocer la convolución, no obstante , simultaneamente se comparará el mismo sistema en phyton, con el fin de comparar las señales resultantes y representaciones gráficas.

1. En primer lugar, se obtuvo un sistema a h[n] = {5600501} y la señal x[n] = {1013097620} para obtener lo siguiente;

      1.1. De manera inicial, vamos a explicar como realizar la convolución de el sistema h(n) y la señal x(n), donde se aplico la fórmula de la convolución discreta, donde h (n) tiene 7 valores y x(n) tiene 10 valores, posterior para sacar la señal y (n )resultante, se tiene que representar la operación como el producto de los polinomios para ver como se distribuyen los términos, es decir, para construir la parte de la ecuación de x(n), se nombró que el índice en la secuencia es el exponente del término, a su vez, para la parte de h(n)se realizó el mismo procedimiento anterior, lo cual se evidenciará en la imagen a continuación;


![WhatsApp Image 2025-02-12 at 21 25 01](https://github.com/user-attachments/assets/75350738-d4b7-494f-9b9f-8b97f255a1d9)



Continuando, se multiplicaron los dos polinomios obtenidos anteriormente,lo que se conoce en señales o algebraicamente como aplicar una convolución discreta, y para resolver esto se planteó una matriz, donde la primera fila es el sistema h(n) y la primera columna es la señal x(n), para obtener los valores internos se multiplicaron los elementos correspondientes al sistema y señal mencionados, para ejemplificar; el primer elemento de x(n) es 5, entonces cada valor de h(n) se va a multiplicar por 5 y se va colocando en la tabla, y así de la misma forma hasta acabar la matriz, por último, al obtener la tabla que se evidenciará a continuación;



![WhatsApp Image 2025-02-12 at 21 28 21](https://github.com/user-attachments/assets/8b4ee8e0-2ed9-4dca-86a1-fd36b2f528b5)



Obteniendo esta matriz, se suman los valores en diagonal, que se encuentran resltados en verde, con el fin de obtener cada termino para la señal y (n) resultante, y de esta forma operamos lo que sea posible, y se obtiene la señal y(n) resultante de la convolución.



   1.2. Se obtuvo la representación gráfica y secuencial a mano, esto para identificar la evolución de la señal en el tiempo, observando picos, crecimientos, o disminución en los patrones de la señal resultante, la primera gráfica es la señal resultante de la convolucion de y(n) y luego se ven la representación gráfica de los vectores  del sistema h(n) y la señal x(n).




<img width="561" alt="Captura de pantalla 2025-02-12 a la(s) 9 17 33 p m" src="https://github.com/user-attachments/assets/945a16c7-3f36-4af1-b710-5c015bb20d21" />
  
![WhatsApp Image 2025-02-12 at 22 04 51](https://github.com/user-attachments/assets/bd256224-8ca0-4261-9e88-5e8145e7ffed)


![WhatsApp Image 2025-02-12 at 22 05 17](https://github.com/user-attachments/assets/ee5f6b7e-5ed5-43f6-be34-572639ff1f63)



   


Para obtener la gráfica de la señal resultante de la convolución y(n), tomé el valor más alto de los datos de la señal resultante y (n) que fue 95 y realice una escala en el eje y de 5 y se enumeraron los datos obtenidos y estos indices fueron colocalos de 1 en 1 en el eje x, de esta forma se hicieron los puntos observados. Ahora en cuanto al análisis, obtenemos que en los primeros valores de n cercanos a 0, la señal tiene valores pqeueños, es decir que los primeros términos de la convolución no generan una respuesta fuerte, a diferencia de n=5 o n=6, donde la señal crece de una forma más pronunciada, y el pico alto se obtiene alrededor de n=9 o 10, que esto quiere decir que en esta posición la suma d elos productos tiene la mayor contribución (como el sistema y la señal afectan a y (n)), después de este pico, se dismiuye otra vez la señal, indicando que la contribución de los valores fue más pequeña, por último cuando la gráfica esta por terminar se vuelve aproximar a 0, donde la convolución ha terminadoy no hay más contribución de los términos desplazados.

De la misma manera, podemos evidenciar que el sistema h(n), actúo como un filtro o respuesta impulso, ya que si h( n)tiene cierto patrón se reflejará directamente en y (n), donde se evidencia como el sistema reacciona a una entrada básica (un pulso o puede ser una delta dirac (delta dirac es una entrada impulso)), a su vez, la gráfica muestra una señal transitoria que quiere decir que la convolución genera un crecimiento progresivo. 



Es importante mencionar que para correr el codigo y que funcione correctamente se deben descargar ciertas cosas, inicialmente en la consola de spyder se deben descargar  librerías de la siguiente manera; pip install numpy matplotlib wfdb scipy, estas son para;

- import numpy as np: es para que permita correr cálculos númericos y arrays en caso de tenerlos.
- import matplotlib.pyplot as plt :permite visualizar los datos
- import wfdb ; esta va a leer y a su vez usar las señales fisiológicas que en este caso es una EEG para implementarlo en un formato estándar.
- Scipy ; es para la parte estadistica más avazada que incluye ;
              - from scipy.fftpack import fft; hace la transformada de                       fourier de una forma rápida , y se usa para analizar en                      este caso la señal eeg. 
            -  from scipy.signal import welch ; on esta se estima la 
               densidad espectral de potencia, también detecta patrones de 
               actividad cerebal, esto lo veremos más adelante




   1.3. Se realizó el mismo procedimiento del item 1.1 pero esta vez usando python, lo que a su vez permite realizar una comparación y observar las dierencias o similitudes.
 

En esta parte se importaron las librerias que se descargaron anteriormente, y a su vez se definieron las señales donde , x (n) es la señal de entrada y h (n) es la repsuesta al impulso, con esto se implemento una función de phyton para calcular la convolución ¨y_n = np.convolve(x_n, h_n)¨ y de esa forma se muestra la convolución resultante, lo cual se evidencia a continuación:



<img width="584" alt="Captura de pantalla 2025-02-12 a la(s) 7 25 13 p m" src="https://github.com/user-attachments/assets/bd26fb9c-2acf-4650-9d6c-f1e24629a964" />



Posterior a esto, se realiza la gráfica de la convoluión, con el fin de observar similitudes o diferencias con el proceso realizado a mano.

 1.4. En este item, se obtuvo una representación gráfica y secuencial en phyton de la señal resultante de la convolución y (n), y los vectores del sistema h (n) y el vetor de la señal x (n); 



<img width="488" alt="Figure 2025-02-12 220304 (0)" src="https://github.com/user-attachments/assets/9dc64ea7-bd92-4376-a5b3-a13c4b5e1df0" />


<img width="488" alt="Figure 2025-02-12 220304 (1)" src="https://github.com/user-attachments/assets/56a281cd-5b20-4c16-bdd3-d6baceab1f73" />


<img width="606" alt="Figure 2025-02-12 220304 (2)" src="https://github.com/user-attachments/assets/d442258a-8b17-4691-ae9e-62a4dda3a182" />

En cuanto al análisis, ambas gráficas muestra lo mismo, es decir una evolución progresiva de los valores, y el pico es en el mismo punto, este método de phyton nos sirve para obtener más precisión ya que python usa valores precisos, y no hay posibles errores de imprecisión como lo puede haber en el caso de la gráfica a mano, de esta forma logramos observar que a pesar de usar dos métodos distintos, se puede comparar, ya que la diferencia entre ambas gráficas no debería ser muy notoria, puesto que es lo mismo. 





      
2. ⁠En segundo lugar, se tenían dos señales, donde se observó si tenian correlación, y a su vez se determinó la representación gráfica y secuencial, lo que se visualiza en el archivo puntob.


En cuanto al código de este punto, se importan las librerias de la misma forma que se mencionó anteriormente, y se establecieron los parámetros de la señal ,la frecuencia de muestreo (cuántas muestras por segundo se toman.), el periodo de muestreo(intervalo entre muestras.), y el vector de tiempo discreto (n rango de valores de 0 a 8 (9 muestras), indicando los instantes de muestreo), en este caso ambas señales tienen la misma frecuencia y se desfasann en 90 grados (ya que el seno y el coseno son funciones ortogonales), se graficaron la correlacion de las señales 



-La señal de EEG completa representa una señal en el dominio del tiempo con un gran número de muestras, se observa un comportamiento regular, con algunos picos inusuales (posibles artefactos o eventos neuronales), artefactos de movimiento (cuando el paciente se movió o parpadeó), ruido en la señal (interferencia de dispositivos electrónicos), actividad neuronal espontánea (picos epilépticos o cambios en el estado cognitivo).



-Se presenta en milivoltios (mV) en el eje vertical y el tiempo en segundos en el eje horizontal.

<img width="719" alt="Figure 2025-02-12 222631 (0)" src="https://github.com/user-attachments/assets/9de48038-cafc-40db-8410-a0010976eb63" />



- Sección de la señal EEG, es una muestra una sección específica de la señal para analizar más detalles, se observa un patrón oscilatorio con variaciones de amplitud.

- Se observa un patrón oscilatorio más claro, con variaciones en amplitud.
El eje vertical sigue en milivoltios (mV) y el eje horizontal muestra un rango de tiempo más acotado.
- Las variaciones de amplitud pueden indicar: cambios en la actividad cerebral (entrada en un estado de relajación, alerta, etc.).
Posible presencia de ritmos específicos (ondas alfa, beta, etc.).

<img width="729" alt="Figure 2025-02-12 224033 (1)" src="https://github.com/user-attachments/assets/776a49d7-d8c6-4c3e-a49b-7f161a38798a" />




Los códigos creados en esta parte del proyecto permiten observar la señal obtenida del sofware PHYSIONET, la cual es electroencefalografía (EEG), que en este caso mide por un método no invasivo los niveles de activación de distintas zonas del cerebro, evaluando  la actividad del cerebro. 

El código carga una señal EMG desde un sofware llamado pyhsionet, donde se busca la parte de ¨data¨,  y se busca la señal a evdienciar que en este caso es EEG, este ejecuta distintos archivos, se debe buscar especificamente el .hea y .data del mismo nombre (ejemplo; EEG-1.hea y EEG-1.data), para posterior, importarla y visualizarla  en un programador llamado pyhton (spyder), que permitira hacer el cálculo de estadísticos importantes como la media, desviación estándar y coeficiente de variación, a su vez se obtiene el gráfico secuencial de la convolución .


Se verifica la funcinalidad del pyhton, y se procederá a descargar la señal como se mencionó anteriormente, asegurandose que tengan el mismo nombre como ya se ejemplificó, y de esta forma se guarda en un archivo que se encuentre en la misma carpeta de el script que en este caso es llamado lab2,y  ejecuta el script de la siguiente forma;  python analisis_emg.py. Para continuar, se interpretan los resultados obtenidos de esto;


   
3.Por último, se realizó la descarga de la señal del software physionet. En github se evidencian los dos archivos del mismo: .dat y .hea, donde se realizó lo siguiente;

   3.1. Se caracterizó la señal en función del tiempo, donde a su vez se calcularon los estadisticos descriptivos, de lo cual podemos evidenciar que.....

   
Se realizan distintas caracterizaciones de la señal, cálculos estadísticos y una ampliación de un segmento específico para un análisis más detallado y más preciso. 


   Media: es una herramienta de estadística esencial, ya que esta indica el promedio que se obtiene al dividir la suma del total de los datos que se tengan entre el total de los mismos, de manera similar, esta proporciona un punto de equilibrio en la distribución de llos diferentes datos.

   
• Desviación estándar ; esta permite medir la dispersión en el conjunto de datos que se este estudiando, y a su vez, se utiliza simultáneamente con la media para determinar los distintos intervalos estadísticos.

<img width="567" alt="Captura de pantalla 2025-02-12 a la(s) 10 30 04 p m" src="https://github.com/user-attachments/assets/239539ac-2208-4448-96dd-05e678444470" />



   3.2. La señal en cuanto a la clasificación es;
   

   3.3. Aplicando la transformada de fourier de la señal, se graficó la transformada y la densidad espectral.....

   <img width="728" alt="Figure 2025-02-12 222631 (3)" src="https://github.com/user-attachments/assets/afcfeefc-93af-46a0-910a-77c04e11e93b" />

<img width="727" alt="Figure 2025-02-12 222631 (2)" src="https://github.com/user-attachments/assets/add3356d-a301-443f-a186-ca225b7a1c2a" />



3.4. Se analizaron los estadistícos descriptivos en función a la frecuencia, teniendo en cuenta que;

Es necesario comprender estos conceptos  de estadísticos descriptivos antes de continuar;
• Frecuencia media; indica el promedio que se obtiene al dividir la suma del total de los datos que se tengan entre el total de los mismos, de manera similar, esta proporciona un punto de equilibrio en la distribución de llos diferentes datos.

• Frecuencia mediana; este es el valor de la mitad de un conjunto de datos, en caso de haber un número total impar es el dato de la mitad, y si es par es el promedio de los valores centrales, y esta se usa cuando los datos se encuentran agrupados en intervalos.

• Desviación estándar ; esta permite medir la dispersión en el conjunto de datos que se este estudiando, y a su vez, se utiliza simultáneamente con la media para determinar los distintos intervalos estadísticos.

• Histograma: Este tipo de grafico, consiste en la representación de una variable cuantitativa por medio de barras, agrupando los datos, donde en el eje x se representan los intervalos de los datos y en el eje y evidencia la frecuencia de los datos en cierto intervalo, es la representación empirica de los datos observados en nuestro caso son las barras grises).

<img width="609" alt="Figure 2025-02-12 222631 (4)" src="https://github.com/user-attachments/assets/45fca27f-ff75-4501-ab66-99c976f88b51" />



Con estos terminos claros, se comprende que respecto a los valores obtenidos, es posible analizar que....................
