"""
scnp_modeling package.

Import modeling utilities and expose them at the package level.
"""

from .__about__ import __version__
from .utils import load_data, save_model, load_model

__all__ = ['__version__', 'load_data', 'save_model', 'load_model']
