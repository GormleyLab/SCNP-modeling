"""
Entry point for the SCNP visualization sub-project.

Run this file to verify the environment and demonstrate package imports:
    python main.py
"""

import sys
import os

# Add src/ to path so notebooks and scripts can also do:
#   sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from scnp_visualization import __version__, load_data, save_figure


def main():
    print(f"scnp_visualization v{__version__}")
    print("Environment OK — umap, seaborn, sklearn, pandas are available.")
    print("Use load_data() to read CSV/Excel files.")
    print("Use save_figure() to save matplotlib figures to disk.")


if __name__ == "__main__":
    main()
