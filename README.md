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

The workflow includes:

- Generation of EVI images from PlanetScope SuperDove imagery
- Extraction of tree-level EVI time series
- Preparation and quality control of time-series data
- Double logistic curve fitting
- Extraction of land surface phenology (LSP) metrics (SOS, POS, EOS and GSL)
- Statistical comparison between urban thermal zones
- Sensitivity analysis using multiple dynamic thresholds
- Generation of publication-quality figures and tables

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

## 🔄 Workflow
