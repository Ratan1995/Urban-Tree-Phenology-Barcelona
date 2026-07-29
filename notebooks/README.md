# Notebook

This directory contains the Google Colab notebook used to reproduce the complete workflow for analyzing the effects of the Urban Heat Island (UHI) on tree phenology in Barcelona.

## Notebook

| File | Description |
|------|-------------|
| `Tree_Phenology.ipynb` | Complete workflow, including data preprocessing, EVI time-series preparation, double logistic curve fitting, extraction of land surface phenology (LSP) metrics, statistical analyses, and figure generation. |

---

## Workflow

The notebook performs the following analyses:

1. Load EVI time-series data.
2. Prepare and clean the datasets.
3. Fit double logistic curves.
4. Extract phenological metrics (SOS, POS, EOS, and GSL).
5. Compare thermal zones.
6. Perform statistical analyses.
7. Conduct sensitivity analysis.
8. Generate publication-quality figures.

---

## Requirements

The notebook requires the Python packages listed in the repository's `requirements.txt` file.

---

## Notes

- The notebook reproduces the analyses presented in the associated manuscript.
- Input datasets are located in the `data/` directory.
- Generated figures are saved in the `figures/` directory.
- Output files are written to the `output/` directory.
