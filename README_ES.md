# Predicción de Recuperación de Oro

## Resumen del Proyecto

Este repositorio contiene un proyecto completo de machine learning para predecir la eficiencia de recuperación de oro en un proceso industrial de beneficio mineral.

El proyecto sigue la especificación del Sprint 13: validar los datos crudos, analizar la dinámica de recuperación, comparar distribuciones entre train y test, eliminar anomalías de concentración y entrenar modelos predictivos usando la métrica final sMAPE.

Se incluyen dos notebooks equivalentes:

- `notebooks/gold_recovery_EN.ipynb`
- `notebooks/gold_recovery_ES.ipynb`

Ambos usan el mismo código, la misma metodología, los mismos resultados y el mismo protocolo de modelado. La única diferencia es el idioma.

---

## Objetivo Técnico y de Negocio

El objetivo es predecir dos variables de recuperación:

- `rougher.output.recovery`
- `final.output.recovery`

Estas variables representan la eficiencia de recuperación en distintas etapas del proceso de purificación de oro.

El modelo final se evalúa con la métrica ponderada sMAPE definida por el proyecto:

```text
final_sMAPE = 0.25 * rougher_sMAPE + 0.75 * final_sMAPE
```

---

## Datos

El proyecto utiliza tres archivos CSV:

```text
data/
├── gold_recovery_train.csv
├── gold_recovery_test.csv
└── gold_recovery_full.csv
```

### Rol de cada dataset

| Archivo | Rol |
|---|---|
| `gold_recovery_train.csv` | Datos de entrenamiento con objetivos |
| `gold_recovery_test.csv` | Variables de prueba sin objetivos |
| `gold_recovery_full.csv` | Dataset fuente completo usado para recuperar objetivos por `date` |

Las observaciones están indexadas por `date`. Esto es importante porque los valores cercanos en el tiempo suelen ser similares y la validación debe respetar el orden temporal.

---

## Restricciones Clave del Proyecto

Este proyecto no es una regresión tabular estándar.

Restricciones importantes:

1. **Dependencia temporal**  
   Los datos están ordenados por tiempo de adquisición.

2. **Diferencia de disponibilidad de variables**  
   Algunas variables presentes en entrenamiento no existen en test porque se miden o calculan posteriormente.

3. **Riesgo de fuga de información**  
   Las variables no disponibles al momento de predicción no deben usarse para entrenar.

4. **Métrica personalizada**  
   La calidad del modelo se mide con sMAPE ponderado, no con RMSE o R².

---

## Metodología

### 1. Carga e Inspección de Datos

Los notebooks cargan:

- datos de entrenamiento
- datos de prueba
- dataset fuente completo

Se inspecciona:

- tamaño de los datasets
- valores faltantes
- filas duplicadas
- cobertura temporal
- disponibilidad de variables

---

### 2. Validación de la Fórmula de Recuperación

Se verifica el cálculo de recuperación rougher con la fórmula:

```text
Recovery = C * (F - T) / (F * (C - T)) * 100
```

Donde:

| Símbolo | Significado |
|---|---|
| `F` | Concentración en la alimentación |
| `C` | Concentración en el concentrado |
| `T` | Concentración en colas |

La recuperación calculada se compara contra `rougher.output.recovery` usando MAE.

Este paso confirma si la columna objetivo es internamente consistente antes de modelar.

---

### 3. Análisis de Variables Faltantes en Test

Los notebooks identifican variables presentes en train pero ausentes en test.

Estas variables se analizan por:

- cantidad
- tipo de dato
- etapa del proceso
- categoría del parámetro

Después se excluyen del entrenamiento porque no estarían disponibles en inferencia real.

---

### 4. Preprocesamiento

El preprocesamiento incluye:

- ordenar observaciones por `date`
- alinear las variables de entrenamiento con las variables de test
- recuperar los objetivos de test desde el dataset completo usando `date`
- imputar valores faltantes con relleno temporal hacia adelante y hacia atrás
- eliminar filas anómalas según concentraciones totales

---

### 5. Análisis Exploratorio

El EDA responde las preguntas obligatorias del proyecto:

#### Concentración de metales por etapa de purificación

Los notebooks analizan cómo cambia la concentración de:

- oro (`Au`)
- plata (`Ag`)
- plomo (`Pb`)

a través de:

- alimentación
- concentrado rougher
- concentrado final

#### Distribución del tamaño de partículas

Se comparan las distribuciones de tamaño de partícula entre train y test para evaluar si la medición del modelo será confiable.

#### Análisis de concentración total

Se calcula la concentración total en:

- materia prima
- concentrado rougher
- concentrado final

Los valores cercanos a cero o anormales se tratan como anomalías y se eliminan cuando corresponde.

---

## Modelado

El proyecto entrena y compara varios modelos:

- Dummy baseline
- Decision Tree Regressor
- Random Forest Regressor

El baseline se incluye para confirmar que el modelo seleccionado aporta valor predictivo real frente a una estrategia ingenua.

---

## Estrategia de Validación

Los notebooks usan `TimeSeriesSplit`, no KFold con mezcla aleatoria.

Esto es clave porque una validación aleatoria puede filtrar información temporal y producir resultados demasiado optimistas.

La validación temporal refleja mejor la estructura del proceso industrial.

---

## Estructura del Repositorio

```text
.
├── data/
│   ├── gold_recovery_full.csv
│   ├── gold_recovery_test.csv
│   └── gold_recovery_train.csv
├── notebooks/
│   ├── gold_recovery_EN.ipynb
│   └── gold_recovery_ES.ipynb
├── reports/
│   ├── figures/
│   ├── portfolio_report_en.md
│   └── portfolio_report_es.md
├── results/
│   └── results_summary.csv
├── src/
│   └── metrics.py
├── INTERVIEW_EXPLANATION_EN.md
├── INTERVIEW_EXPLANATION_ES.md
├── README_EN.md
├── README_ES.md
├── requirements.txt
└── .gitignore
```

---

## Cómo Ejecutar

1. Clonar o descargar el repositorio.
2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Abrir cualquiera de los notebooks:

```bash
jupyter notebook notebooks/gold_recovery_ES.ipynb
```

o

```bash
jupyter notebook notebooks/gold_recovery_EN.ipynb
```

4. Ejecutar todas las celdas en orden.

---

## Conclusiones Clave

- Validar el objetivo antes de modelar es indispensable.
- Las variables disponibles en test definen el espacio válido de entrenamiento.
- Eliminar anomalías por concentración total mejora la estabilidad.
- La validación temporal es esencial para este proyecto.
- Random Forest ofrece una base no lineal sólida como modelo final.

---

## Siguientes Pasos

Mejoras posibles:

- Agregar variables temporales con rezagos.
- Probar modelos de gradient boosting.
- Hacer búsqueda sistemática de hiperparámetros.
- Analizar importancia de variables y drift.
- Convertir el flujo del notebook en un pipeline reproducible.

---

## Nota

Este repositorio está estructurado como caso de portafolio. Demuestra validación de datos, prevención de fuga de información, preprocesamiento con criterio de dominio, métrica personalizada, validación temporal y comparación de modelos.
