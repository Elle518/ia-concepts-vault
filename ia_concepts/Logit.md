---
type: concept
tags:
  - ml
  - llms
  - review
---

## Definición

Un ***logit*** es una puntuación numérica sin normalizar que produce un modelo antes de convertirla en probabilidad.

En clasificación, cada clase puede tener un *logit*. En un [[Modelo del lenguaje|modelo de lenguaje]], cada token del vocabulario recibe un *logit* antes de aplicar [[Softmax|softmax]] para obtener una distribución de probabilidad.

Un *logit* no es todavía una probabilidad. Es más parecido a una preferencia interna del modelo: cuanto mayor es el *logit* de una clase o token respecto a los demás, más probable será que el modelo lo elija después de normalizar.

Lo importante no suele ser el valor absoluto del *logit*, sino su diferencia con otros *logits*.

## Relación con probabilidades

En un problema multiclase, el modelo puede producir un vector de logits:

$$z = [z_1, z_2, \dots, z_K]$$

donde cada $z_i$ corresponde a una clase. Después, normalmente se aplica softmax para convertir esos valores en probabilidades:

$$p_i = \frac{\exp(z_i)}{\sum_j \exp(z_j)}$$

En clasificación binaria, el término *logit* también se usa para referirse al **log-odds**:

$$\text{logit}(p) = \log \frac{p}{1-p}$$

En modelos generativos, los *logits* del vocabulario se pueden modificar antes de muestrear el siguiente token. Por ejemplo, la [[Temperatura|temperatura]] divide los *logits* antes de aplicar softmax.

Los logits pueden ser negativos, positivos o cero. No tienen que sumar 1 y no están acotados entre 0 y 1.

Las probabilidades, en cambio, sí están normalizadas:

- cada probabilidad está entre 0 y 1
- todas las probabilidades de las clases suman 1

Por eso, decir que un *logit* vale 8 no significa que la probabilidad sea 8. Hay que compararlo con el resto de logits.

## Errores comunes

- Confundir *logits* con probabilidades.
- Interpretar un *logit* de forma aislada, sin compararlo con los demás.
- Olvidar que softmax es sensible a diferencias entre *logits*, no solo a sus valores absolutos.
- Aplicar softmax dos veces antes de calcular una pérdida como cross-entropy.
- Pensar que un *logit* alto siempre implica una predicción bien calibrada.

## Preguntas

#flashcards/ml #flashcards/llms

**¿Qué es un *logit*?**
?
![[#Definición]]

**¿Cómo se relacionan los*logits* con las probabilidades?**
?
![[#Relación con probabilidades]]

**¿Qué errores comunes aparecen al trabajar con *logits*?**
?
![[#Errores comunes]]
