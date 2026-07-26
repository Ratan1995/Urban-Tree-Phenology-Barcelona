# Assessing the Urban Heat Island Effect on Tree Phenology Using High-Resolution Satellite Imagery

*A reproducible Python workflow for investigating the influence of the Urban Heat Island (UHI) on urban tree phenology using high-resolution PlanetScope SuperDove imagery.*

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab&logoColor=white)
![PlanetScope](https://img.shields.io/badge/Data-PlanetScope-2E8B57)
![EVI](https://img.shields.io/badge/Vegetation%20Index-EVI-228B22)
![Barcelona](https://img.shields.io/badge/Study%20Area-Barcelona-E67E22)
![Urban Heat Island](https://img.shields.io/badge/Theme-Urban%20Heat%20Island-D35454)
![Remote Sensing](https://img.shields.io/badge/Field-Remote%20Sensing-6C5CE7)
![License](https://img.shields.io/badge/License-MIT-F1C40F)

**Author:** Ratan Chandra Bhowmick  
**Supervisors:** Robbe Neyns & Prof. Frank Canters  
**Affiliation:** Department of Geography, Vrije Universiteit Brussel (VUB)

---

## 📖 Overview

Urban Heat Islands (UHIs) alter the seasonal growth and development of urban vegetation by modifying local microclimatic conditions. This repository provides a complete and reproducible workflow for extracting Enhanced Vegetation Index (EVI) time series from PlanetScope SuperDove imagery and analysing the land surface phenology of urban tree species across contrasting urban thermal environments in Barcelona, Spain.

---

## 🌍 Study Area

**Location:** Barcelona, Spain

**Study Species**

- *Platanus × hispanica*
- *Celtis australis*
- *Styphnolobium japonicum*

**Satellite Data**

- PlanetScope SuperDove (3 m spatial resolution)

**Vegetation Index**

- Enhanced Vegetation Index (EVI)

**Programming Language**

- Python

**Notebook**

- Google Colab

## 🔄 Methodology Workflow

The overall workflow adopted in this study is illustrated below.

<p align="center">
  <img src="figures/methodology_workflow.png" alt="Methodology Workflow" width="1000">
</p>
## 📂 Repository Structure

```text
.
├── data/
├── docs/
├── figures/
├── notebooks/
├── output/
├── scripts/
│   ├── 01_create_evi_images.py
│   ├── 02_extract_evi_timeseries.py
│   ├── 03_prepare_timeseries.py
│   ├── 04_fit_double_logistic.py
│   ├── 05_extract_lsp_metrics.py
│   ├── 06_statistics.py
│   ├── 07_sensitivity_analysis.py
│   └── 08_make_figures.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```
## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Ratan1995/Urban-Tree-Phenology-Barcelona.git
cd Urban-Tree-Phenology-Barcelona
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```
## 📦 Data

The analysis requires the following datasets:

| Dataset | Description |
|---------|-------------|
| PlanetScope SuperDove | High-resolution multispectral imagery (3 m) |
| Barcelona Tree Inventory | Urban tree inventory containing tree locations and species information |
| Landsat 8 Collection 2 Level-2 | Land Surface Temperature (LST) used for thermal zonation |

> **Note:** The original PlanetScope imagery is proprietary and therefore cannot be redistributed through this repository. Users should obtain PlanetScope imagery through an appropriate license before running the workflow.
