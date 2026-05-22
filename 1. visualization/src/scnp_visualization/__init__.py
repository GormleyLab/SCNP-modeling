"""
scnp_visualization package.

Import visualization utilities and expose them at the package level.
"""

from .__about__ import __version__
from .utils import load_data, save_figure

__all__ = ['__version__', 'load_data', 'save_figure']
