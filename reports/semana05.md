# Semana 05 - Marco Tecnológico de la IA

# Explicación
Esta semana trabajé con **sistemas híbridos de inteligencia artificial**, que combinan reglas expertas, recuperación de información con TF‑IDF y clasificación de texto.  
El objetivo fue demostrar que el sistema no solo responde, sino que **justifica la decisión con evidencia trazable**.

# Lo que hice
- Creé un archivo `data/base_conocimiento.txt` con 8 entradas de soporte técnico.  
- Definí 5 reglas expertas en `src/semana05_sistema_hibrido.py`.  
- Entrené un clasificador con 15 ejemplos etiquetados.  
- Implementé la función `answer(query)` para devolver reglas disparadas, documento recuperado, similitud y clase predicha.  
- Generé el reporte automático `reports/semana05.md` con tres consultas de prueba.

# Explicación del código
- **Reglas expertas:** condiciones simples que activan acciones explicables (ej. “dns” → revisar conectividad).  
- **Base de conocimiento:** archivo de texto con casos frecuentes, usado para recuperación de evidencia.  
- **TF‑IDF y similitud coseno:** convierten consultas en vectores y buscan el documento más parecido.  
- **Clasificador:** modelo de regresión logística entrenado con frases etiquetadas para predecir categorías (hardware, red, seguridad, rendimiento).  
- **Reporte:** función que guarda resultados en Markdown para auditoría.

# Resultados
Ejemplo de salida en `reports/semana05.md`:

# Consulta 1
- Entrada: El equipo está caliente  
- Reglas: revisar_ventilación  
- Evidencia: Equipo caliente → revisar ventilación  
- Similitud: 0.796  
- Clase: hardware  

# Consulta 2
- Entrada: Internet se cae y aparece error DNS  
- Reglas: revisar_conectividad  
- Evidencia: Internet cae → revisar DNS o enlace  
- Similitud: 0.735  
- Clase: red  

# Consulta 3
- Entrada: No puedo iniciar sesión con mi cuenta  
- Reglas: revisar_acceso  
- Evidencia: Cuenta bloqueada → revisar permisos  
- Similitud: 0.398  
- Clase: seguridad  

# Tabla de distribución por categorías

|-----------------|------------------------|-------------------------------------------------------------------------------|
| **Categoría**   | **Situación**          | **Acción recomendada**                                                        |
|-----------------|------------------------|-------------------------------------------------------------------------------|
| **Hardware**    | Equipo caliente        | Revisar ventilación, limpiar ventilador, ajustar tornillería, lubricar piezas |
|                 | Sistema no arranca     | Revisar disco duro, BIOS, fuente de poder, cables internos                    |
|                 | Pantalla azul          | Revisar drivers, ejecutar diagnóstico RAM, comprobar hardware                 |
|                 | Error de impresora     | Revisar conexión USB, reinstalar drivers, comprobar tinta/tóner               |
|                 | Disco lleno            | Liberar espacio, eliminar temporales, ampliar almacenamiento                  |
|                 | CPU sobrecargado       | Cerrar procesos innecesarios, optimizar tareas, revisar ventilación           |
|-----------------|------------------------|-------------------------------------------------------------------------------|
| **Red**         | Internet cae           | Revisar DNS, router, modem, cableado                                          |
|                 | Red lenta              | Revisar router, cableado, optimizar Wi-Fi, comprobar interferencias           |
|                 | Router desconectado    | Reiniciar router, verificar conexión física                                   |
|-----------------|------------------------|-------------------------------------------------------------------------------|
| **Seguridad**   | Cuenta bloqueada       | Revisar permisos, restablecer credenciales, verificar políticas               |
|                 | Usuario sin permisos   | Asignar privilegios adecuados, revisar roles                                  |
|                 | Virus detectado        | Ejecutar antivirus, aislar archivos, actualizar definiciones                  |
|-----------------|------------------------|-------------------------------------------------------------------------------|
| **Rendimiento** | App lenta              | Revisar CPU, memoria, disco; cerrar procesos; optimizar inicio automático     |
|                 | Aplicación no responde | Reiniciar proceso, reinstalar aplicación, verificar compatibilidad            |
| **Software**    | Actualización fallida  | Reinstalar sistema, aplicar rollback, verificar espacio en disco              |
|-----------------|------------------------|-------------------------------------------------------------------------------|



### Conclusiones
El sistema híbrido logra responder consultas de soporte técnico con trazabilidad:  
- **Reglas disparadas** muestran la lógica aplicada.  
- **Evidencia recuperada** conecta con la base documental.  
- **Similitud** cuantifica la confianza textual.  
- **Clase predicha** categoriza el problema.  

La principal limitación es que con pocos ejemplos el clasificador puede equivocarse, por lo que se recomienda ampliar la base de conocimiento y los datos de entrenamiento.


