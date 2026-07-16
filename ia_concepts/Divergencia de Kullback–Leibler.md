---
type: concept
tags:
  - ml
  - stats
  - review
---

## Definición

La **divergencia de Kullback-Leibler** o ***KL divergence*** mide cuánto se diferencia una distribución de probabilidad de otra.

En *machine learning* se usa para comparar distribuciones, regularizar modelos probabilísticos y entrenar modelos generativos.

No es una distancia simétrica, es decir, comparar $P$ con $Q$ no da necesariamente lo mismo que comparar $Q$ con $P$.

La KL divergence mide cuánta información extra se pierde o se paga al usar una distribución aproximada $Q$ cuando la distribución real es $P$.

Si $Q$ asigna baja probabilidad a eventos que $P$ considera probables, la divergencia aumenta. Por eso se interpreta como una penalización por representar mal una distribución.

## Fórmula

Para distribuciones discretas:

$$D_{KL}(P || Q) = \sum_x P(x) \log \frac{P(x)}{Q(x)}$$

La expectativa se toma bajo $P$, por eso importa mucho dónde $P$ concentra probabilidad.

Si $P(x) > 0$ y $Q(x) = 0$, la divergencia se vuelve problemática porque $Q$ está ignorando un evento posible bajo $P$.

## Uso en machine learning

La *KL divergence* aparece en:

- [[Modelo probabilístico|modelos probabilísticos]]
- [[Variational inference|variational inference]]
- [[VAEs]]
- [[Distillation|distillation]]
- [[Proximal Policy Optimization|regularización de políticas en RLHF]] y [[DPO]]
- comparación de distribuciones de salida de modelos

También está relacionada con [[Cross-entropy|cross-entropy]] y [[Entropía|entropía]].


## Preguntas

#flashcards/ml

**¿Qué mide la divergencia de Kullback-Leibler?**
?
![[#Definición]]

**¿Cómo se calcula la KL divergence?**
?
![[#Fórmula]]

**¿Dónde aparece la KL divergence en *machine learning*?**
?
![[#Uso en machine learning]]
