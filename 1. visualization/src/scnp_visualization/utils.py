"""
Utility functions for the scnp_visualization package.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt


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


def save_figure(fig: plt.Figure, filepath: str, dpi: int = 300) -> None:
    """
    Save a matplotlib figure to disk.

    Args:
        fig:      The matplotlib Figure to save.
        filepath: Output path (e.g. 'imgs/umap.png').
        dpi:      Resolution in dots per inch. Default 300.
    """
    os.makedirs(os.path.dirname(filepath) or ".", exist_ok=True)
    fig.savefig(filepath, dpi=dpi, bbox_inches="tight")
    print(f"Figure saved to {filepath}")
