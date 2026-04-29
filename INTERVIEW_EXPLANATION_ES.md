# Explicación para Entrevista — Predicción de Recuperación de Oro

## Versión de 30 segundos
Este proyecto predice recuperación de oro en dos etapas usando datos industriales indexados por tiempo. El mayor riesgo era la fuga de información, porque algunas variables de train no existen en test. Validé la fórmula de recuperación, eliminé variables no disponibles, limpié anomalías, usé sMAPE ponderado y evalué modelos con TimeSeriesSplit. Random Forest fue el mejor modelo entre las opciones probadas.

## Versión de 2 minutos
El proyecto usa tres datasets: train, test y full. El conjunto de test no tiene objetivos y tampoco contiene algunas variables que se miden después en el proceso. Para hacer el modelado realista, entrené solo con variables disponibles en test. Los objetivos de test se recuperaron desde el dataset full usando la fecha.

Antes de modelar, validé la fórmula de recuperación rougher recalculándola y comparándola contra el objetivo mediante MAE. Después analicé cómo cambian las concentraciones de metales por etapa, comparé las distribuciones de tamaño de partícula entre train y test, y eliminé filas con concentraciones totales anómalas.

Para modelar, implementé la métrica sMAPE y el score final ponderado. Como los datos son temporales, usé TimeSeriesSplit en lugar de KFold aleatorio. Esto evita una validación demasiado optimista por fuga temporal.

## Preguntas esperables

### ¿Por qué no usar todas las variables de train?
Porque muchas variables exclusivas de train se miden después del momento de predicción. Usarlas sería fuga de información.

### ¿Por qué TimeSeriesSplit?
Porque las observaciones están indexadas por tiempo y los valores cercanos están correlacionados. Mezclar aleatoriamente contamina la validación.

### ¿Por qué Random Forest?
Captura relaciones no lineales, funciona como baseline robusto y no requiere escalado fuerte ni supuestos lineales.

### ¿Qué mejorarías?
Agregaría features con rezagos, probaría gradient boosting, ajustaría hiperparámetros y monitorearía drift.
