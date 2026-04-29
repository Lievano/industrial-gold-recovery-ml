"""
Custom evaluation metrics for the Gold Recovery project.

This module contains the sMAPE implementation used in both notebooks.
The final score follows the project definition:

    final_sMAPE = 0.25 * rougher_sMAPE + 0.75 * final_sMAPE
"""

from __future__ import annotations

import numpy as np


def smape(y_true, y_pred) -> float:
    """Calculate Symmetric Mean Absolute Percentage Error.

    Parameters
    ----------
    y_true : array-like
        True target values.
    y_pred : array-like
        Predicted target values.

    Returns
    -------
    float
        sMAPE value in percentage points.
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    denominator = (np.abs(y_true) + np.abs(y_pred)) / 2
    diff = np.abs(y_true - y_pred)

    return np.mean(np.where(denominator == 0, 0, diff / denominator)) * 100


def final_smape(y_true, y_pred) -> float:
    """Calculate the weighted final sMAPE for rougher and final recovery.

    Parameters
    ----------
    y_true : array-like of shape (n_samples, 2)
        True values for rougher and final recovery.
    y_pred : array-like of shape (n_samples, 2)
        Predicted values for rougher and final recovery.

    Returns
    -------
    float
        Weighted final sMAPE.
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    rougher_score = smape(y_true[:, 0], y_pred[:, 0])
    final_score = smape(y_true[:, 1], y_pred[:, 1])

    return 0.25 * rougher_score + 0.75 * final_score
