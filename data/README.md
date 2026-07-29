# Data

This directory contains the datasets used and generated during the analysis of urban tree phenology in Barcelona.

## Dataset Description

| File | Description |
|------|-------------|
| `Platanus_EVI_Timeseries.csv` | EVI time-series extracted from PlanetScope imagery for *Platanus × hispanica*. |
| `Celtis_EVI_Timeseries.csv` | EVI time-series extracted from PlanetScope imagery for *Celtis australis*. |
| `Japonicum_EVI_Timeseries.csv` | EVI time-series extracted from PlanetScope imagery for *Styphnolobium japonicum*. |
| `Platanus_LST_4zones.csv` | Mean annual land surface temperature (LST) values and thermal zone assignments for *Platanus × hispanica*. |
| `Celtis_LST_4zones.csv` | Mean annual land surface temperature (LST) values and thermal zone assignments for *Celtis australis*. |
| `Japonicum_LST_4zones.csv` | Mean annual land surface temperature (LST) values and thermal zone assignments for *Styphnolobium japonicum*. |
| `Platanus_LSP_Tree.csv` | Tree-level land surface phenology (LSP) metrics derived from the fitted EVI time series for *Platanus × hispanica*. |
| `Celtis_LSP_Tree.csv` | Tree-level land surface phenology (LSP) metrics derived from the fitted EVI time series for *Celtis australis*. |
| `Japonicum_LSP_Tree.csv` | Tree-level land surface phenology (LSP) metrics derived from the fitted EVI time series for *Styphnolobium japonicum*. |
| `Mann_Whitney_U_Results.csv` | Results of the Mann–Whitney U test comparing phenological metrics between the coolest (Zone 1) and warmest (Zone 4) thermal zones. |
| `Shapiro_Wilk_Results.csv` | Shapiro–Wilk normality test results for the extracted phenological metrics. |
| `Table4_Factorial_Model.csv` | Statistical summary of the factorial model used to evaluate the effects of species and thermal zones on phenological metrics. |

---

## Data Sources

The datasets were generated from the following sources:

- **PlanetScope SuperDove imagery (3 m)** – EVI time-series extraction.
- **Landsat 8 Collection 2 Level-2** – Annual land surface temperature (LST).
- **Barcelona Open Data Tree Inventory** – Tree locations and species information.

---

## Notes

- The EVI time-series were extracted for individual trees using PlanetScope imagery acquired between **February 2024 and February 2025**.
- Trees were assigned to four thermal zones using annual mean LST derived from Landsat 8.
- Phenological metrics (SOS, POS, EOS, and GSL) were extracted from double logistic fitted EVI curves using the **20% dynamic threshold method**.
- Statistical analyses include Shapiro–Wilk normality tests and Mann–Whitney U tests to evaluate differences between thermal zones.

