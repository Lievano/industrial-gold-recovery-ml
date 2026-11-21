# Gold Recovery Prediction

## Project Summary

This repository contains a complete machine learning project for predicting gold recovery efficiency in an industrial mineral processing pipeline.

The project follows the Sprint 13 specification: validate raw process data, analyze recovery dynamics, compare train/test distributions, remove anomalous concentration values, and train predictive models using the required final sMAPE metric.

Two equivalent notebooks are included:

- `notebooks/gold_recovery_EN.ipynb`
- `notebooks/gold_recovery_ES.ipynb`

They use the same code, same methodology, same outputs, and same modeling protocol. The only difference is language.

---

## Business and Technical Objective

The objective is to predict two recovery targets:

- `rougher.output.recovery`
- `final.output.recovery`

These targets represent recovery efficiency at different stages of the gold purification process.

The final model is evaluated using the project-specific weighted sMAPE:

```text
final_sMAPE = 0.25 * rougher_sMAPE + 0.75 * final_sMAPE
```

---

## Dataset

The project uses three CSV files:

```text
data/
├── gold_recovery_train.csv
├── gold_recovery_test.csv
└── gold_recovery_full.csv
```

### Dataset roles

| File | Role |
|---|---|
| `gold_recovery_train.csv` | Training data with targets |
| `gold_recovery_test.csv` | Test features without targets |
| `gold_recovery_full.csv` | Full source dataset used to recover test targets by `date` |

The observations are indexed by `date`. This matters because measurements close in time are expected to be similar, and validation must respect temporal ordering.

---

## Core Project Constraints

This project is not a standard tabular regression problem.

Important constraints:

1. **Temporal dependency**  
   Data points are ordered by acquisition time.

2. **Feature availability mismatch**  
   Some variables present in the training set are absent from the test set because they are measured or calculated later.

3. **Data leakage risk**  
   Features unavailable at prediction time must not be used for training.

4. **Custom metric**  
   Model quality is evaluated with weighted sMAPE, not RMSE or R².

---

## Methodology

### 1. Data Loading and Inspection

The notebooks load:

- training data
- test data
- full source data

They inspect:

- dataset shapes
- missing values
- duplicated rows
- date coverage
- feature availability

---

### 2. Recovery Formula Validation

The rougher recovery calculation is verified using:

```text
Recovery = C * (F - T) / (F * (C - T)) * 100
```

Where:

| Symbol | Meaning |
|---|---|
| `F` | Feed concentration |
| `C` | Concentrate concentration |
| `T` | Tail concentration |

The calculated recovery is compared against `rougher.output.recovery` using MAE.

This step confirms whether the target column is internally consistent before modeling.

---

### 3. Missing Feature Analysis

The notebooks identify features available in train but missing from test.

These features are analyzed by:

- count
- data type
- process stage
- parameter category

They are excluded from model training because they would not be available during real inference.

---

### 4. Preprocessing

The preprocessing stage includes:

- sorting observations by `date`
- aligning training features with test features
- recovering test targets from the full dataset using `date`
- imputing missing values using temporal forward/backward filling
- removing anomalous rows based on total concentration values

---

### 5. Exploratory Data Analysis

The EDA answers the required project questions:

#### Metal concentration by purification stage

The notebooks analyze how the concentration of:

- gold (`Au`)
- silver (`Ag`)
- lead (`Pb`)

changes across:

- feed
- rougher concentrate
- final concentrate

#### Feed particle size distribution

Train and test feed-size distributions are compared to evaluate whether the model evaluation is reliable.

#### Total concentration analysis

The notebooks calculate total concentration across:

- raw feed
- rougher concentrate
- final concentrate

Near-zero or abnormal totals are treated as anomalies and removed from both train and test-aligned samples where applicable.

---

## Modeling

The project trains and compares multiple models:

- Dummy baseline
- Decision Tree Regressor
- Random Forest Regressor

The baseline is included to verify that the selected model adds predictive value beyond a naive strategy.

---

## Validation Strategy

The notebooks use `TimeSeriesSplit`, not shuffled KFold.

This is important because shuffled validation can leak temporal information and produce overly optimistic scores.

Temporal validation better reflects the structure of the industrial process.

---

## Repository Structure

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

## How to Run

1. Clone or download this repository.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Open either notebook:

```bash
jupyter notebook notebooks/gold_recovery_EN.ipynb
```

or

```bash
jupyter notebook notebooks/gold_recovery_ES.ipynb
```

4. Run all cells from top to bottom.

---

## Key Takeaways

- Target validation is necessary before modeling.
- Test-set feature availability defines the valid training feature space.
- Outlier removal based on concentration totals improves modeling stability.
- Time-aware validation is essential for this project.
- Random Forest provides a strong non-linear baseline for the final model.

---

## Suggested Next Steps

Potential improvements:

- Add lag-based temporal features.
- Test gradient boosting models.
- Add systematic hyperparameter tuning.
- Track feature importance and model drift.
- Convert the notebook workflow into a reproducible pipeline.

---

## Author Notes

This repository is structured as a portfolio-ready machine learning case study. It demonstrates data validation, leakage prevention, domain-aware preprocessing, custom metric implementation, temporal validation, and model comparison.
