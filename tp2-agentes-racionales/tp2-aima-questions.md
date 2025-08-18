# Trabajo Práctico Número 2 Inteligencia Artificial
## AIMA Questions

<p align="center">**2.10- **Consider a modified version of the vacuum environment in Exercise 2.8, in which the
agent is penalized one point for each movement.**</p>
<p align="left">**a. Can a simple reflex agent be perfectly rational for this environment? Explain.**</p> 
Respuesta: El agente no va a ser un agente racional perfecto, ya que no va a maximizar su perfomance debido a que por cada movimiento que realize se le descontará un punto. Quiere decir que una vez haya terminado de limpiar las celdas, se moverá infinitamente de manera que contará con puntos negativos. Al no maximizar su medidad de desempeño o perfomance no consideramos a este tipo de agente racional.

<p align="left">**b. What about a reflex agent with state? Design such an agent.**</p>
Respuesta: Si el agente tiene un estado interno en donde guarda las posiciones de las celdas las cuales ya han sido limpiadas, por lo tanto vamos a considerarlo racional. La idea es que al agente por cada celda que limpie, guarde en memoria la posición de la celda la cual limpio. Una vez se encuentre en otra celda y decida el siguiente movimiento, si la celda a moverse ya ha sido limpiada (lo corrobora usando su memoria interna) no debe moverse hacia esa celda por lo tanto no se le descontará puntos por movmiento.

<p align="left">**c. How do your answers to a and b change if the agent’s percepts give it the clean/dirty
status of every square in the environment?**</p>
Respuesta: La respuesta del a si al agente le damos la percepción total del entorno para saber si las celdas estan sucias,seguiría sin poder maximiar su perfomance ya que por más que sepa los spots donde haya o no haya suciedad, se seguirá moviendo mientras siga perdiendo puntos. A diferencia de la respuesta b, el agente si podrá maximizar su perfomance ya que al saber el estado de cada celda, no hará ningún movimiento inecesario permitiendole no perder puntos de penalización.



<p align="center">**2.11- **Consider a modified version of the vacuum environment in Exercise 2.8, in which the
geography of the environment—its extent, boundaries, and obstacles—is unknown, as is the
initial dirt configuration. (The agent can go Up and Down as well as Left and Right.)**</p>
<p align="left">**a. Can a simple reflex agent be perfectly rational for this environment? Explain.**</p> 
Respuesta: La respuesta es no ya que el agente necesitará memoria y un modelado más amplio del mundo para poder explorar lo desconocido. Además si se encuentra con obstáculos como paredes o se encuentra con un tiempo prefijado para limpiar, el agente puede llegar a perderse o puede no llegar a completar todo el entorno limpio en el tiempo predefinido.

<p align="left">**b. Can a simple reflex agent with a randomized agent function outperform a simple reflex
agent? Design such an agent and measure its performance on several environments.**</p> 
Respuesta: 