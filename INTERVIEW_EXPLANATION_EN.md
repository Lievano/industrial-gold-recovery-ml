# Interview Explanation — Gold Recovery Prediction

## 30-second version
This project predicts gold recovery at two process stages using time-indexed industrial data. The biggest risk was leakage, because some training features are not available in the test set. I validated the recovery formula, removed unavailable features, cleaned anomalies, used weighted sMAPE, and evaluated models with TimeSeriesSplit. Random Forest was selected as the strongest model among the tested options.

## 2-minute version
The project uses three datasets: train, test, and full. The test set lacks targets and also lacks features that are measured later in the process. To make the modeling realistic, I trained only with features available in test. I recovered test targets from the full dataset using the timestamp.

Before modeling, I validated the rougher recovery formula by recalculating it and comparing it with the provided target using MAE. Then I analyzed metal concentration changes across purification stages, compared feed-size distributions between train and test, and removed rows with abnormal total concentrations.

For modeling, I implemented the required sMAPE metric and the weighted final score. Since the data is temporal, I used TimeSeriesSplit instead of shuffled KFold. This avoids optimistic validation caused by temporal leakage.

## Questions I would expect

### Why not use all train features?
Because many train-only features are measured after the prediction point. Using them would create leakage.

### Why TimeSeriesSplit?
Because the observations are time-indexed and neighboring observations are correlated. Random shuffling would contaminate validation.

### Why Random Forest?
It captures non-linear relationships, performs well as a robust baseline, and does not require heavy scaling or strong linear assumptions.

### What would you improve?
I would add lag features, test gradient boosting, tune hyperparameters, and monitor drift.
