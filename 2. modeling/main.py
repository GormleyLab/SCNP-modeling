"""
Entry point for the SCNP modeling sub-project.

Run this file to verify the environment and demonstrate package imports:
    python main.py
"""

import sys
import os

# Add src/ to path so notebooks and scripts can also do:
#   sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from scnp_modeling import __version__, load_data, save_model, load_model


def main():
    print(f"scnp_modeling v{__version__}")
    print("Environment OK — xgboost, shap, umap, sklearn are available.")
    print("Use load_data() to read CSV/Excel files.")
    print("Use save_model() / load_model() to persist trained models to models/.")


if __name__ == "__main__":
    main()
