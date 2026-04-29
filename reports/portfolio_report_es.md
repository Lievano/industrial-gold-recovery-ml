# Reporte de Portafolio — Predicción de Recuperación de Oro

## Por qué importa este proyecto
Este caso simula un problema industrial real de ML donde se debe predecir con información incompleta. El reto principal no es solo la precisión, sino elegir correctamente las variables bajo restricciones operativas.

## Decisiones técnicas principales
- Se usaron solo variables disponibles en el conjunto oficial de test.
- Se recuperaron los objetivos de test desde el dataset completo usando `date`.
- Se utilizó validación temporal en lugar de validación aleatoria.
- Se eliminaron filas anómalas de concentración después del análisis exploratorio.
- Se evaluaron modelos con el sMAPE ponderado definido por el proyecto.

## Señal más fuerte de portafolio
El proyecto maneja explícitamente la fuga de información. En datos industriales, usar variables downstream no disponibles puede hacer que un modelo parezca preciso aunque sea inútil en producción.

## Interpretación en producción
Una versión productiva requeriría:
- contratos de disponibilidad de variables,
- validaciones programadas de calidad de datos,
- monitoreo de drift,
- estrategia de reentrenamiento,
- registro de errores cuando se observen recuperaciones reales.
