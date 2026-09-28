# Semana 07 - Representaciones del reconocimiento

## Explicación
Esta semana trabajé con **tres formas de representar un mismo fenómeno**:  
- **Numérica** (vectores y distancias).  
- **Simbólica** (hechos y reglas).  
- **Autómata** (patrones secuenciales).  

El objetivo fue demostrar que la elección de la representación condiciona qué operaciones son posibles y qué información se pierde, manteniendo trazabilidad conceptual y práctica.

---

## Lo que hice
- Creé el archivo `src/semana07_representaciones.py` con tres bloques: numérico, simbólico y autómata.  
- Ejecuté el código para validar las salidas esperadas.  
- Documenté ventajas, limitaciones y pérdida de información en este reporte.  
- Integré evidencia de ejecución y análisis comparativo.  
- Realicé commit `semana07-representaciones`.

---

## Explicación del código
- **Bloque numérico:** convierte observaciones en vectores y calcula la distancia con `np.linalg.norm`.  
- **Bloque simbólico:** usa conjuntos de hechos y reglas explícitas (`issubset`) para concluir situaciones como `riesgo_termico`.  
- **Bloque autómata:** define estados y transiciones para reconocer secuencias que terminan en `01`.  

Cada bloque responde a un tipo de problema: comparación cuantitativa, razonamiento explicable y validación secuencial.

---

## Resultados

### Representación numérica
- Distancia numérica: 2.062


### Representación simbólica
- Conclusión simbólica: riesgo_termico

### Autómata
1101 aceptada: True
1110 aceptada: False
0001 aceptada: True

---


---

## Tabla comparativa

| **Representación** | **Ventajas**                        | **Limitaciones**                  | **Pérdida de información**         |
|---------------------|-------------------------------------|-----------------------------------|------------------------------------|
| **Numérica**        | Precisa, fácil de calcular          | Difícil de explicar en lenguaje natural | Significado semántico              |
| **Simbólica**       | Explicable, reglas claras           | Menos flexible con datos continuos | Valores numéricos exactos          |
| **Autómata**        | Ideal para secuencias y patrones    | Limitado a reglas definidas        | Contexto fuera de la secuencia     |

---

## Conclusiones
El sistema logra representar y reconocer fenómenos desde tres perspectivas:  
- **Numérica:** útil para cálculos y comparaciones cuantitativas.  
- **Simbólica:** aporta explicaciones claras y reglas trazables.  
- **Autómata:** permite validar secuencias y estados.  

La principal limitación es que cada representación **pierde información distinta**, por lo que en sistemas híbridos conviene combinar al menos dos enfoques para mayor robustez.
