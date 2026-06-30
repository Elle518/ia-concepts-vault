---
type: concept
tags:
  - agents
  - review
---

## Definición

***Prompt caching*** es una técnica que permite reutilizar la parte estable de un *prompt* o conversación para reducir coste y latencia en llamadas posteriores al modelo.

En [[Agente de IA|agentes]], suele aplicarse a *system prompts*, *[[Agent config files|config files]]*, *[[Workflow files reutilizables|workflows]]* cargados y otra información que se repite en cada turno.

Si el agente tiene que leer las mismas reglas en cada paso, no conviene pagar el coste completo cada vez. El caché guarda esa parte estable y en turnos posteriores la reusa con descuento.

## Explicación técnica

El primer *request* envía el *prompt* completo y el proveedor lo escribe en caché. Las llamadas siguientes reutilizan ese *prompt* mientras el caché siga vivo. Esto reduce el coste y puede mejorar la [[Latencia|latencia]], pero no elimina los tokens de la [[Ventana de contexto|ventana de contexto]].

## Time-to-live

La limitación práctica es el TTL (*time-to-live*). Si la sesión queda inactiva demasiado tiempo, el caché expira y la siguiente llamada vuelve a pagar el coste de escritura. Además, aunque el caché abarate tokens, un contexto largo puede seguir degradando calidad por [[Context rot|context rot]].

Algunas herramientas o proveedores permiten elegir un TTL más largo. Un TTL más largo significa que la caché permanece activa durante más tiempo, pero su creación puede resultar más costosa. Un TTL más corto puede ser más económico, pero la caché puede caducar antes. Por lo tanto, la elección depende de tu flujo de trabajo.

## Errores comunes

- Pensar que *prompt caching* mejora la capacidad de razonamiento.
- Usarlo como excusa para meter instrucciones enormes.
- Ignorar la expiración del TTL.
- Confundir ahorro económico con un mejor contexto.

## Preguntas

#flashcards/agents 

**¿Qué es *prompt caching*?**
?
![[#Definición]]

**¿Cómo funciona el *prompt caching*?**
?
![[#Explicación técnica]]

**¿Qué es el TTL en *prompt caching*?**
?
![[#Time-to-live]]

**¿Qué errores se suelen cometer al usar *prompt caching*?**
?
![[#Errores comunes]]

