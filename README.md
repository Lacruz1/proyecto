```mermaid
diagrama de flujo TD
A([Inicio]) --> B[/seleccionar dificultad/]
B --> C{¿Opción Válida?}
C -- No --> B
C -- Si --> D[Generar Número Aleatorio nC]
D --> E[Inicializar Intentos]
E --> F{¿Intentos > 0?}
F -- No --> G[Mostrar: Perdiste]
... (el resto de tu código) ...
```
