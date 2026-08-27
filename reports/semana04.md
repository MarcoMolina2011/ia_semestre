# Semana 04 - Marco tecnológico de la IA

## Explicación
Esta semana trabajé con algoritmos de búsqueda y juegos adversariales.

## Lo que hice
- Implementé A* para encontrar rutas en una cuadrícula.
- Implementé Minimax para decidir jugadas en tres en línea.
- Probé ambos algoritmos con ejemplos simples.

## Explicación del código
- En A*: estado = posición en la cuadrícula, acción = movimiento, meta = llegar al objetivo, costo = pasos, heurística = distancia Manhattan.
- En Minimax: estado = tablero, acción = jugada, función de utilidad = ganar/perder/empatar, árbol de decisiones = posibles jugadas, poda alfa-beta = optimización.

## Resultados
- A* encontró una ruta válida y calculó su costo.
- Minimax devolvió la mejor jugada para X en el tablero dado.

## Conclusiones
- A* muestra cómo una heurística guía la búsqueda.
- Minimax evidencia cómo anticipar decisiones de un oponente.
- Ambos algoritmos son base para sistemas más complejos de IA.
