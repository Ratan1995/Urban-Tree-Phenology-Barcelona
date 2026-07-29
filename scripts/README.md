# Scripts

This directory contains the Python scripts used to process PlanetScope imagery, extract vegetation indices, derive land surface phenology (LSP) metrics, perform statistical analyses, and generate the results presented in this repository.

## Processing Workflow

The scripts should be executed in the following order:

| Step | Script | Description |
|------|--------|-------------|
| 1 | `01_create_evi_images.py` | Calculates Enhanced Vegetation Index (EVI) images from PlanetScope SuperDove imagery. |
| 2 | `02_extract_evi_timeseries.py` | Extracts tree-level EVI time-series for each species using the Barcelona tree inventory. |
| 3 | `03_prepare_timeseries.py` | Cleans, organizes, and prepares the EVI time-series for curve fitting. |
| 4 | `04_fit_double_logistic.py` | Fits a six-parameter double logistic model to the EVI time-series. |
| 5 | `05_extract_lsp_metrics.py` | Extracts land surface phenology (LSP) metrics, including Start of Season (SOS), Peak of Season (POS), End of Season (EOS), and Growing Season Length (GSL), using the 20% dynamic threshold method. |
| 6 | `06_statistics_Analysis.py` | Performs statistical analyses, including Shapiro–Wilk normality tests and Mann–Whitney U tests, to compare phenological metrics between thermal zones. |
| 7 | `07_sensitivity_analysis.py` | Evaluates the sensitivity of phenological metrics to different dynamic threshold values and generates the corresponding sensitivity curves. |

---

## Input Data

The scripts require the following datasets:

- PlanetScope SuperDove imagery
- Barcelona Open Data Tree Inventory
- Landsat 8 Collection 2 Level-2 Land Surface Temperature (LST)

These datasets are located in the `data/` directory.

---

## Outputs

Running the scripts produces:

- EVI time-series for each tree species
- Double logistic fitted curves
- Land surface phenology (LSP) metrics
- Statistical test results
- Publication-quality figures

Outputs are stored in the `output/` and `figures/` directories.

---

## Notes

- Scripts are designed to be executed sequentially.
- Intermediate outputs from one script serve as inputs for subsequent scripts.
- Required Python packages are listed in the repository's `requirements.txt` file.
