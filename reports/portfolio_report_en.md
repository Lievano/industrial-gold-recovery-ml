# Portfolio Report — Gold Recovery Prediction

## Why this project matters
This case study simulates a real industrial ML problem where prediction must be made with incomplete information. The main challenge is not only model accuracy, but correct feature selection under operational constraints.

## Main technical decisions
- Used only features available in the official test set.
- Recovered test targets from the full source table by `date`.
- Used temporal validation instead of shuffled validation.
- Removed anomalous concentration rows after exploratory analysis.
- Evaluated models with the project-specific weighted sMAPE.

## Strongest portfolio signal
The project explicitly handles data leakage. In industrial data, using unavailable downstream variables can make a model look accurate while being unusable in production.

## Production interpretation
A production version would require:
- feature availability contracts,
- scheduled data quality checks,
- drift monitoring,
- model retraining strategy,
- logging of prediction errors once true recoveries become available.
