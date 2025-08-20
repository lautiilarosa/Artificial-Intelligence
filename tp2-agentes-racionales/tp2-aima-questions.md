# Trabajo Práctico Número 2 Inteligencia Artificial
## AIMA Questions

### **2.10-** Consider a modified version of the vacuum environment in Exercise 2.8, in which the agent is penalized one point for each movement.

#### **a. Can a simple reflex agent be perfectly rational for this environment? Explain.**

**Respuesta:** El agente no va a ser un agente racional perfecto, ya que no va a maximizar su performance debido a que por cada movimiento que realice se le descontará un punto. Quiere decir que una vez haya terminado de limpiar las celdas, se moverá infinitamente de manera que contará con puntos negativos. Al no maximizar su medida de desempeño o performance no consideramos a este tipo de agente racional.

#### **b. What about a reflex agent with state? Design such an agent.**

**Respuesta:** Si el agente tiene un estado interno en donde guarda las posiciones de las celdas las cuales ya han sido limpiadas, por lo tanto vamos a considerarlo racional. La idea es que al agente por cada celda que limpie, guarde en memoria la posición de la celda la cual limpió. Una vez se encuentre en otra celda y decida el siguiente movimiento, si la celda a moverse ya ha sido limpiada (lo corrobora usando su memoria interna) no debe moverse hacia esa celda por lo tanto no se le descontará puntos por movimiento.

#### **c. How do your answers to a and b change if the agent's percepts give it the clean/dirty status of every square in the environment?**

**Respuesta:** La respuesta del a si al agente le damos la percepción total del entorno para saber si las celdas están sucias, seguiría sin poder maximizar su performance ya que por más que sepa los spots donde haya o no haya suciedad, se seguirá moviendo mientras siga perdiendo puntos. A diferencia de la respuesta b, el agente si podrá maximizar su performance ya que al saber el estado de cada celda, no hará ningún movimiento innecesario permitiéndole no perder puntos de penalización.

### **2.11-** Consider a modified version of the vacuum environment in Exercise 2.8, in which the geography of the environment—its extent, boundaries, and obstacles—is unknown, as is the initial dirt configuration. (The agent can go Up and Down as well as Left and Right.)

#### **a. Can a simple reflex agent be perfectly rational for this environment? Explain.**

**Respuesta:** La respuesta es no ya que el agente necesitará memoria y un modelado más amplio del mundo para poder explorar lo desconocido. Además si se encuentra con obstáculos como paredes o se encuentra con un tiempo prefijado para limpiar, el agente puede llegar a perderse o puede no llegar a completar todo el entorno limpio en el tiempo predefinido.

#### **b. Can a simple reflex agent with a randomized agent function outperform a simple reflex agent? Design such an agent and measure its performance on several environments.**

**Respuesta:** No, si es cierto que con entornos más pequeños podemos considerar que el agente pueda de alguna manera, igualar la perfomance a un agente que reflexivo simple. pero mientras más grande sea el entorno, la perfomance del random se verá más ineficiente a diferencia del reflexivo.

#### **c. Can you design an environment in which your randomized agent will perform poorly? Show your results.**

**Respuesta:** Si armamos entornos grandes de alrededor de 64x64 o 128x128 , nuestro agente random tendra un rendimiento bastante pobre. Si los armamos veremos que el agente no podrá cumplir más del 3% por ciento de suciedad que se puedan encontrar en las celdas.

#### **d. Can a reflex agent with state outperform a simple reflex agent? Design such an agent and measure its performance on several environments. Can you design a rational agent of this type?**

**Respuesta:** Si ya que al tener guardado las posiciones que tengamos de cada celda con suciedad, podremos evitar movimientos de tal manera que nos lleven a celdas que ya han sido limpiadas, además de que evitaremos chocarnos contra paredes. 