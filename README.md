# SCNP Modeling & Visualization

**Gormley Lab — Single-Chain Nanoparticle (SCNP) analysis pipeline**

This project is split into two independent sub-projects, each with its own
Python virtual environment, source package, and Jupyter notebooks.

---

## 📁 Project Structure

```
SCNP Modeling/
├── README.md
├── LICENSE
├── .gitignore
├── requirements_visualization.txt   # packages for 1. visualization
├── requirements_modeling.txt        # packages for 2. modeling
├── imgs/                            # shared images and plot outputs
│
├── 1. visualization/                # UMAP, Kratky plots, dimensionality reduction
│   ├── .venv_visualization/         # Python 3.9 virtual environment
│   ├── data/                        # raw and processed data files
│   ├── notebooks/                   # Jupyter notebooks
│   ├── main.py                      # entry point — verifies environment
│   └── src/
│       └── scnp_visualization/      # Python package
│           ├── __about__.py         # version and metadata
│           ├── __init__.py
│           └── utils.py             # load_data(), save_figure()
│
└── 2. modeling/                     # XGBoost, SHAP, ML pipeline
    ├── .venv_models/                # Python 3.13 virtual environment
    ├── data/                        # raw and processed data files
    ├── models/                      # saved trained models (.pkl)
    ├── notebooks/                   # Jupyter notebooks
    ├── main.py                      # entry point — verifies environment
    └── src/
        └── scnp_modeling/           # Python package
            ├── __about__.py         # version and metadata
            ├── __init__.py
            └── utils.py             # load_data(), save_model(), load_model()
```

---

## 🚀 Quick Start

### 1. Visualization environment (Python 3.9)

```powershell
cd "1. visualization"
.\.venv_visualization\Scripts\Activate.ps1
python main.py
```

### 2. Modeling environment (Python 3.13)

```powershell
cd "2. modeling"
.\.venv_models\Scripts\Activate.ps1
python main.py
```

---

## 🔧 Setting Up from Scratch

### Visualization venv

```powershell
cd "1. visualization"
py -3.9 -m venv .venv_visualization
.\.venv_visualization\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r ..\requirements_visualization.txt
```

### Modeling venv

```powershell
cd "2. modeling"
py -3.13 -m venv .venv_models
.\.venv_models\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r ..\requirements_modeling.txt
```

---

## 📓 Using in Jupyter Notebooks

Select the correct kernel in VS Code for each notebook:

| Sub-project | Kernel (interpreter) |
|---|---|
| `1. visualization/notebooks/` | `.venv_visualization\Scripts\python.exe` |
| `2. modeling/notebooks/` | `.venv_models\Scripts\python.exe` |

To import the local package inside a notebook, add to the first cell:

```python
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.getcwd()), "src"))
```

---

## 📦 Key Packages

| Environment | Key packages |
|---|---|
| `scnp_visualization` (Py 3.9) | `umap-learn`, `seaborn`, `scikit-learn`, `pandas`, `matplotlib` |
| `scnp_modeling` (Py 3.13) | `xgboost`, `shap`, `umap-learn`, `scikit-learn`, `pandas` |

---

## 🤝 Contributing

This project is maintained by the Gormley Lab.
See [GL-template](https://github.com/GormleyLab/GL-template) for the base project template.
