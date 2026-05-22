"""
Utility functions for the scnp_modeling package.
"""

import os
import pickle
import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:
    """
    Load a CSV or Excel file into a pandas DataFrame.

    Args:
        filepath: Path to the data file (.csv or .xlsx).

    Returns:
        Loaded DataFrame.
    """
    ext = os.path.splitext(filepath)[-1].lower()
    if ext == ".csv":
        return pd.read_csv(filepath)
    elif ext in (".xlsx", ".xls"):
        return pd.read_excel(filepath)
    else:
        raise ValueError(f"Unsupported file type: {ext}")


def save_model(model, filepath: str) -> None:
    """
    Serialize a trained model to disk with pickle.

    Args:
        model:    Trained model object (e.g. XGBoost, sklearn estimator).
        filepath: Output path inside models/ (e.g. 'models/xgb_model.pkl').
    """
    os.makedirs(os.path.dirname(filepath) or ".", exist_ok=True)
    with open(filepath, "wb") as f:
        pickle.dump(model, f)
    print(f"Model saved to {filepath}")


def load_model(filepath: str):
    """
    Load a serialized model from disk.

    Args:
        filepath: Path to the .pkl model file.

    Returns:
        Deserialized model object.
    """
    with open(filepath, "rb") as f:
        model = pickle.load(f)
    print(f"Model loaded from {filepath}")
    return model
