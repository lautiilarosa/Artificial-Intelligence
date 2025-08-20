**Reporte TP2 Inteligencia Artificial**

Agente Reflexivo: Se desarrolló un agente reflexivo simple en el cual sus sensores permiten identificar si en la celda correspondiente hay suciedad, por lo cual el agente procede a limpiarlo. Su patrón de movimiento es bastante sencillo ya que después de limpiar la celda el agente se moverá de manera aleatoria a cualquier casilla que se encuentre a la derecha,izquierda,abajo o arriba.

Agente Random: Como lo especifica, es un agente que toma todas decisiones de manera aleatoria, de tal manera que si en la celda que se encuentra hay o no tierra , el agente limpiará o no hará nada y se moverá a otra celda también de manera aleatoria como el agente reflexivo. Por lo tanto para cada movimiento y en una celda con suciedad hay un 50% de que el agente vaya a limpiarla.

**Análisis del rendimiento a través de gráficos**

Se especificaron una variedad de entornos para poder probar los agentes los cuales se categorizan por tamaño y por porcentaje de suciedad. Se encuentra disponibles \[“2x2”,”4x4”,”8x8”,”16x16”,”32x32”,”64x64”,”128x128”\] y dirt rate o porcentaje de suciedad de 0.1,0.2,0.4 y 0.8 por ciento. Para cada combinación que existe (alrededor de 28), se hicieron 10 pruebas con distinta semilla para cada agente, de tal manera para posteriormente analizar en un mismo entorno el desempeño o performance de los 2 agentes y comparar.

![][image1]

Vemos en este gráfico la performance de cada agente por entorno que tenemos. Verá que hasta un tamaño 8x8 los agentes parecen tener un desempeño bastante equivalente, pero a medida que aumentamos el tamaño del entorno, el agente random parece ser más deficiente que un agente reflexivo simple. Esto es más que nada por el simple hecho de que el agente random en celdas que contienen suciedad, puede o no puede limpiarla algo que el agente reflexivo lo hace en un 100%. 

Por más que el agente reflexivo simple parezca más eficiente que el random, no quiere decir que este primero sea un agente que pueda cumplir con la cuota total de celdas con suciedad. Lo observamos en el siguiente gráfico:  
![][image2]

Como podrá observar, los agentes hasta el entorno 8x8, parecen limpiar el 100% de las celdas que contienen suciedad (salvando las 2x2 que no tienen), pero si aumentamos el tamaño del entorno, verá que los agentes de a poco dejarán celdas sin limpiar llegando incluso a porcentajes bajos como 5%.  
Cabe recalcar que en entornos más grandes como 128x128, tiene un total de 16384 celdas en total y si contamos el 80 por ciento de celdas con suciedad nos daría un total de alrededor de 13107 celdas, y los agentes tienen un límite de 1000 movimientos por lo tanto sería imposible cubrir todo el terreno. Por supuesto si se desarrolla un agente más inteligente podríamos cubrir un porcentaje un poco más elevado.

**Conclusión:** Podemos concluir que los 2 agentes en sí a medida que el entorno pasa a ser más complejo se vuelven bastante ineficientes, pero en cuando a su performance en ciertos entornos más medianos y chicos podemos decir que el agente reflexivo es mucho más efectivo por cuestiones de que a la hora de encontrarse una celda, este decide limpiarla, a diferencia de uno random.

[image1]: ./images/promedioporentorno.png

[image2]: ./images/dirtrateporagente.png