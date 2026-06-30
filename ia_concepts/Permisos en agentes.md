---
type: concept
tags:
  - agents
  - review
---

## Definición

Los **permisos en [[Agente de IA|agentes]]** son reglas de allow/deny que controlan qué herramientas, archivos, comandos o acciones puede ejecutar un agente sin aprobación humana.

Funcionan como una capa operativa entre el [[Bucle de un agente|agent loop]] y el entorno real.

Un agente optimiza para terminar la tarea. Si algo le bloquea, puede intentar atajos peligrosos. Los permisos definen qué atajos están prohibidos incluso cuando parecen resolver el problema.

## Niveles de configuración

Una configuración práctica suele tener dos niveles:

- **Reglas de proyecto**: comandos seguros y repetibles como tests, lint o lecturas comunes
- **Reglas de usuario u organización**: deny-list para secretos, borrados destructivos, force-push, instalación remota o comandos con red

Algunos runtimes añaden un clasificador de permisos que decide si una acción se permite automáticamente o requiere revisión humana. Esta capa no es perfecta, pero combinada con [[Sandboxing de agentes|sandboxing]] y hooks reduce la fricción sin abrir acceso total.

## Errores comunes

- Aprobar manualmente todo hasta volverse impracticable.
- Permitir comandos amplios como `chmod`, `rm` o `curl | sh`.
- No separar permisos de proyecto y permisos personales.
- Confiar en permisos sin registrar lo que se ejecuta.

## Preguntas

#flashcards/agents

**¿Qué son los permisos en agentes?**
?
![[#Definición]]

**¿Qué diferencia hay entre permisos de proyecto y permisos de usuario en agentes?**
?
![[#Niveles de configuración]]

**¿Qué errores comunes se cometen al configurar permisos en agentes?**
?
![[#Errores comunes]]
