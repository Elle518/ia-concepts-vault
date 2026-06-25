---
type: concept
tags:
  - llms
  - nlp
  - review
---

## Definición

***Top-p sampling***, también llamado ***nucleus sampling***, es una estrategia de [[Parámetros de decoding|decoding]] en la que el modelo solo puede elegir el siguiente token entre el conjunto mínimo de tokens cuya probabilidad acumulada alcanza un umbral $p$.

En lugar de fijar un número exacto de candidatos, como en [[Top-k sampling|top-k sampling]], *top-p* adapta dinámicamente el tamaño del conjunto de tokens posibles en cada paso.

## Utilidad

La intuición es permitir variedad cuando hay varias continuaciones razonables, pero restringir la generación cuando el modelo está muy seguro.

Si la distribución está muy concentrada, quizá basten pocos tokens para alcanzar $p$. Si la distribución está más repartida, el conjunto de candidatos será más grande.

Por ejemplo, con $p = 0.9$, el modelo conserva los tokens más probables hasta que su suma de probabilidades llega al 90%. Después muestrea solo dentro de ese subconjunto.

## Explicación técnica

En cada paso de generación, el modelo calcula una distribución de probabilidad sobre el vocabulario. Con *top-p sampling*:

1. se ordenan los tokens de mayor a menor probabilidad,
2. se añaden tokens al conjunto candidato hasta alcanzar una probabilidad acumulada $p$,
3. se descarta el resto del vocabulario,
4. se normalizan las probabilidades de los tokens conservados,
5. se muestrea el siguiente token.

Esto hace que el número de candidatos varíe según el contexto. En una predicción muy clara, el núcleo puede ser pequeño. En una predicción abierta, puede contener más tokens.

## Comparación con top-k

La diferencia principal es que [[Top-k sampling|top-k]] fija el número de tokens candidatos, mientras que *top-p* fija una masa de probabilidad.

*Top-k* responde a la pregunta: “¿entre cuántos tokens dejamos elegir al modelo?”. *Top-p* responde a: “¿cuánta probabilidad total queremos conservar?”.

En la práctica, *top-p* suele ser más flexible, aunque ambos parámetros pueden combinarse con [[Temperatura|temperatura]].

## Errores comunes

- Pensar que $p = 1$ siempre es mejor. Con $p = 1$, no se filtra prácticamente nada del vocabulario.
- Usar un $p$ demasiado bajo y eliminar alternativas razonables, haciendo la salida más rígida.
- Usar un $p$ demasiado alto en tareas que requieren respuestas precisas, aumentando la variabilidad.
- Ajustar *top-p* sin revisar la temperatura, porque ambos afectan a la diversidad de la generación.

## Preguntas

#flashcards/llms #flashcards/nlp

**¿Qué es *top-p sampling* o *nucleus sampling*?**
?
![[#Definición]]

**¿Cuál es la utilidad detrás de *top-p sampling*?**
?
![[#Utilidad]]

**¿Cómo se calcula *top-p sampling*?**
?
![[#Explicación técnica]]

**¿En qué se diferencia *top-p* de *top-k*?**
?
![[#Comparación con top-k]]

**¿Qué errores comunes hay al usar *top-p sampling*?**
?
![[#Errores comunes]]
