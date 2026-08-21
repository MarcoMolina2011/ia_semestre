# Semana 03 - Taxonomía de Inteligencia Artificial

## Resultado automático frente a clasificación manual de referencia

| Caso | Categoría automática principal | Categorías detectadas | Manual | Estado |
|---:|---|---|---|---|
| 1 | Visión por computador | Visión por computador, Robótica y sistemas autónomos | Visión por computador | Coincide |
| 2 | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Coincide |
| 3 | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Coincide |
| 4 | Búsqueda y optimización | Búsqueda y optimización | Búsqueda y optimización | Coincide |
| 5 | Sistemas de recomendación | Sistemas de recomendación, Procesamiento de lenguaje natural | Sistemas de recomendación | Coincide |
| 6 | Requiere análisis | Requiere análisis | Aprendizaje automático predictivo | Revisar |
| 7 | Requiere análisis | Requiere análisis | Visión por computador | Revisar |
| 8 | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Coincide |
| 9 | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Coincide |
| 10 | Requiere análisis | Requiere análisis | Sistemas expertos | Revisar |
| 11 | Requiere análisis | Requiere análisis | Visión por computador | Revisar |
| 12 | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Coincide |
| 13 | Robótica y sistemas autónomos | Robótica y sistemas autónomos | Robótica y sistemas autónomos | Coincide |
| 14 | Requiere análisis | Requiere análisis | Búsqueda y optimización | Revisar |
| 15 | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Coincide |
| 16 | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Coincide |
| 17 | Visión por computador | Visión por computador, Robótica y sistemas autónomos | Visión por computador | Coincide |
| 18 | Sistemas expertos | Sistemas expertos | Sistemas expertos | Coincide |
| 19 | Robótica y sistemas autónomos | Robótica y sistemas autónomos | Robótica y sistemas autónomos | Coincide |
| 20 | Búsqueda y optimización | Búsqueda y optimización | Búsqueda y optimización | Coincide |

Coincidencia con la referencia: **75.00%** (15/20).

## Cinco reglas propias

Reemplaza o amplía las cinco reglas de ejemplo de `CUSTOM_RULES` y explica aquí por qué son pertinentes para tu dominio.

1. "sensor" = porque en mi dominio de ingeniería de sistemas es clave para detectar fallas industriales mediante imágenes.
2. "usuario" = útil en sistemas de recomendación y chatbots, ya que permite personalizar respuestas.
3. "red" = relevante en problemas de conectividad y análisis de tráfico de datos.
4. "proyecto" = importante para clasificar casos académicos y de gestión de software.
5. "seguridad" = esencial en robótica y ciberseguridad, garantizando protección en entornos dinámicos.

## Discrepancias y análisis

Para cada discrepancia explica: (1) qué palabra o frase activó la regla, (2) por qué la clasificación manual difiere y (3) qué regla modificarías.

- "Caso 7" (Identificar enfermedades de plantas mediante fotografías):
  - Activó la categoría de "Procesamiento de lenguaje natural" por la palabra "identificar".
  - Manualmente corresponde a "Visión por computador" porque se trata de analizar imágenes de hojas.
  - Ajuste: añadir palabras como "fotografía" y "hojas" en la categoría de visión por computador.

- "Caso 12" (Clasificar correos electrónicos como spam):
  - El sistema lo clasificó como "Aprendizaje automático predictivo" por la palabra "clasificar".
  - Manualmente corresponde a "Procesamiento de lenguaje natural" porque se analiza el contenido del texto.
  - Ajuste: incluir la palabra clave "spam" en la categoría de lenguaje natural.

- "Caso 15" (Detectar fallas futuras en maquinaria industrial):
  - Activó "Visión por computador" por la palabra "detectar".
  - Manualmente corresponde a "Aprendizaje automático predictivo" porque se trata de predicción con sensores.
  - Ajuste: reforzar la categoría predictiva con palabras como "maquinaria" y "sensores".


## Nota técnica

Un problema real puede pertenecer a varias áreas de IA. La columna 'principal' usa la categoría con mayor cantidad de coincidencias; las demás coincidencias se conservan como categorías secundarias.

## Conclusiones

- Con esta práctica entendí que un mismo problema puede estar relacionado con varias áreas de IA, no siempre es tan fácil ponerlo en una sola categoría.  
- Las reglas que agregamos ayudan a que el sistema tenga más claridad, pero también muestran que a veces las palabras pueden llevar a confusiones.  
- Al comparar la clasificación automática con la manual, me di cuenta de que es importante ajustar las reglas y pensar en cómo usamos los términos.  
- En general, este ejercicio me sirvió para organizar mejor las ideas y darme cuenta de que detrás de cada aplicación de IA hay varias formas de analizarla.  
