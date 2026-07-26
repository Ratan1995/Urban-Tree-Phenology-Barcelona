# ==========================================Platanus x hispanica ========================================
# Load the input data.

import numpy as np
import pandas as pd

df = pd.read_csv(
    "/content/drive/MyDrive/Colab Notebooks/Platanus_EVI_Timeseries.csv"
)

# Prepare the EVI time series.

evi_columns = [col for col in df.columns if col.isdigit()]
dates = pd.to_datetime(evi_columns, format="%Y%m%d")
elapsed_days = (dates - dates.min()).days.values
t = elapsed_days / elapsed_days.max()

# Extract LSP metrics for each tree.

tree_results = []

for _, row in df.iterrows():

    try:
        tree_id = row["codi"]
        zone = row["LST_zone"]
        y = row[evi_columns].values.astype(float)

        # Skip trees with too many missing values.
        mask = np.isfinite(y)
        if mask.sum() < 10:
            continue

        t_fit = t[mask]
        y_fit = y[mask]

        # Fit the double logistic model.
        params = fit_double_logistic(t_fit, y_fit)

        t_smooth = np.linspace(0, 1, 1200)
        y_smooth = double_logistic(t_smooth, *params)
        days = t_smooth * 365

        # Calculate the 20% dynamic threshold.
        threshold = (
            y_smooth.min()
            + 0.20 * (y_smooth.max() - y_smooth.min())
        )

        pos_idx = np.argmax(y_smooth)
        sos_idx = np.where(y_smooth >= threshold)[0][0]
        eos_idx = np.where(y_smooth >= threshold)[0][-1]

        tree_results.append({
            "codi": tree_id,
            "LST_zone": zone,
            "SOS": days[sos_idx],
            "POS": days[pos_idx],
            "EOS": days[eos_idx],
            "GSL": days[eos_idx] - days[sos_idx],
        })

    except Exception:
        continue

# Save the results.

tree_results = pd.DataFrame(tree_results)

print(tree_results.head())

print(f"\nSuccessful trees: {len(tree_results)}")
print(f"Failed trees: {len(df) - len(tree_results)}")

tree_results.to_csv(
    "/content/drive/MyDrive/Colab Notebooks/Platanus_LSP_Tree.csv",
    index=False
)

==========================================Celtis Australis ========================================
# Load the species time series.

import numpy as np
import pandas as pd

df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Celtis_EVI_Timeseries.csv")

# Remove the BOM character if it exists.
df.columns = df.columns.str.replace("ï»¿", "", regex=False)

# Prepare the EVI time series.

evi_columns = [col for col in df.columns if col.isdigit()]
dates = pd.to_datetime(evi_columns, format="%Y%m%d")
elapsed_days = (dates - dates.min()).days.values
t = elapsed_days / elapsed_days.max()

# Extract LSP metrics for each tree.

tree_results = []

for _, row in df.iterrows():

    tree_id = row["codi"]
    zone = row["LST_zone"]
    y = row[evi_columns].astype(float).values

    # Skip trees with too many missing values.
    if np.isfinite(y).sum() < 20:
        continue

    try:
        params = fit_double_logistic(t, y)

        t_smooth = np.linspace(0, 1, 2000)
        y_smooth = double_logistic(t_smooth, *params)

    except Exception:
        continue

    days = t_smooth * elapsed_days.max()

    # Calculate the 20% dynamic threshold.
    threshold = y_smooth.min() + 0.20 * (y_smooth.max() - y_smooth.min())

    pos_idx = np.argmax(y_smooth)

    before = np.arange(pos_idx)
    after = np.arange(pos_idx, len(y_smooth))

    sos_idx = before[np.where(y_smooth[before] >= threshold)[0][0]]
    eos_idx = after[np.where(y_smooth[after] >= threshold)[0][-1]]

    tree_results.append({
        "codi": tree_id,
        "LST_zone": zone,
        "SOS": days[sos_idx],
        "POS": days[pos_idx],
        "EOS": days[eos_idx],
        "GSL": days[eos_idx] - days[sos_idx],
    })

# Save the results.

tree_results = pd.DataFrame(tree_results)

print(tree_results.head())
print(f"\nSuccessful trees: {len(tree_results)}")
print(f"Failed trees: {len(df) - len(tree_results)}")

tree_results.to_csv(
    "/content/drive/MyDrive/Colab Notebooks/Celtis_LSP_Tree.csv",
    index=False,
)

========================================== Styphnolobium japonicum ========================================
# Load the input data.

import numpy as np
import pandas as pd

df = pd.read_csv(
    "/content/drive/MyDrive/Colab Notebooks/Japonicum_EVI_Timeseries.csv"
)

# Remove the BOM character if it exists.
df.columns = df.columns.str.replace("ï»¿", "", regex=False)

# Prepare the EVI time series.

evi_columns = [col for col in df.columns if col.isdigit()]
dates = pd.to_datetime(evi_columns, format="%Y%m%d")
elapsed_days = (dates - dates.min()).days.values
t = elapsed_days / elapsed_days.max()

# Extract LSP metrics for each tree.

tree_results = []

for _, row in df.iterrows():

    tree_id = row["codi"]
    zone = row["LST_zone"]
    y = row[evi_columns].astype(float).values

    # Skip trees with too many missing values.
    if np.isfinite(y).sum() < 20:
        continue

    try:
        params = fit_double_logistic(t, y)

        t_smooth = np.linspace(0, 1, 2000)
        y_smooth = double_logistic(t_smooth, *params)

    except Exception:
        continue

    days = t_smooth * elapsed_days.max()

    # Calculate the 20% dynamic threshold.
    threshold = (
        y_smooth.min()
        + 0.20 * (y_smooth.max() - y_smooth.min())
    )

    pos_idx = np.argmax(y_smooth)

    before = np.arange(pos_idx)
    after = np.arange(pos_idx, len(y_smooth))

    sos_idx = before[np.where(y_smooth[before] >= threshold)[0][0]]
    eos_idx = after[np.where(y_smooth[after] >= threshold)[0][-1]]

    tree_results.append({
        "codi": tree_id,
        "LST_zone": zone,
        "SOS": days[sos_idx],
        "POS": days[pos_idx],
        "EOS": days[eos_idx],
        "GSL": days[eos_idx] - days[sos_idx],
    })

# Save the results.

tree_results = pd.DataFrame(tree_results)

print(tree_results.head())

print(f"\nSuccessful trees: {len(tree_results)}")
print(f"Failed trees: {len(df) - len(tree_results)}")

tree_results.to_csv(
    "/content/drive/MyDrive/Colab Notebooks/Japonicum_LSP_Tree.csv",
    index=False
)

========================================== Mann - Whitney U Test ========================================
# Load the individual tree LSP datasets.

import pandas as pd
from scipy.stats import mannwhitneyu

files = [
    (
        "/content/drive/MyDrive/Colab Notebooks/Platanus_LSP_Tree.csv",
        r"(a) $\it{Platanus\ \times\ hispanica}$",
    ),
    (
        "/content/drive/MyDrive/Colab Notebooks/Celtis_LSP_Tree.csv",
        r"(b) $\it{Celtis\ australis}$",
    ),
    (
        "/content/drive/MyDrive/Colab Notebooks/Japonicum_LSP_Tree.csv",
        r"(c) $\it{Styphnolobium\ japonicum}$",
    ),
]

metrics = ["SOS", "POS", "EOS", "GSL"]

results = []

# Compare LSP metrics between Zone 1 and Zone 4.

for file_path, species in files:

    df = pd.read_csv(file_path)

    for metric in metrics:

        zone1 = df.loc[df["LST_zone"] == 1, metric].dropna()
        zone4 = df.loc[df["LST_zone"] == 4, metric].dropna()

        U, p = mannwhitneyu(
            zone1,
            zone4,
            alternative="two-sided",
        )

        z1_median = zone1.median()
        z1_q1 = zone1.quantile(0.25)
        z1_q3 = zone1.quantile(0.75)

        z4_median = zone4.median()
        z4_q1 = zone4.quantile(0.25)
        z4_q3 = zone4.quantile(0.75)

        if p < 0.001:
            sig = "***"
        elif p < 0.01:
            sig = "**"
        elif p < 0.05:
            sig = "*"
        else:
            sig = "ns"

        results.append({
            "Species": species,
            "Metric": metric,
            "Zone 1 (Median [IQR])":
                f"{z1_median:.2f} ({z1_q1:.2f}–{z1_q3:.2f})",
            "Zone 4 (Median [IQR])":
                f"{z4_median:.2f} ({z4_q1:.2f}–{z4_q3:.2f})",
            "U statistic": round(U, 2),
            "p-value": p,
            "Significance": sig,
        })

# Save the Mann–Whitney U test results.

results = pd.DataFrame(results)

results["p-value"] = results["p-value"].apply(
    lambda p: "<0.001" if p < 0.001 else f"{p:.4f}"
)

print(results)

results.to_csv(
    "/content/drive/MyDrive/Colab Notebooks/Mann_Whitney_U_Results.csv",
    index=False,
)

print("\nMann_Whitney_U_Results.csv saved successfully.")

========================================== Shapiro–Wilk Normality Test ========================================
# Load the individual tree LSP datasets.

import pandas as pd
from scipy.stats import shapiro

files = [
    (
        "/content/drive/MyDrive/Colab Notebooks/Platanus_LSP_Tree.csv",
        r"(a) $\it{Platanus\ \times\ hispanica}$",
    ),
    (
        "/content/drive/MyDrive/Colab Notebooks/Celtis_LSP_Tree.csv",
        r"(b) $\it{Celtis\ australis}$",
    ),
    (
        "/content/drive/MyDrive/Colab Notebooks/Japonicum_LSP_Tree.csv",
        r"(c) $\it{Styphnolobium\ japonicum}$",
    ),
]

metrics = ["SOS", "POS", "EOS", "GSL"]

normality_results = []

# Perform the Shapiro–Wilk normality test.

for file_path, species in files:

    df = pd.read_csv(file_path)

    for metric in metrics:

        statistic, p = shapiro(df[metric].dropna())

        normality_results.append({
            "Species": species,
            "Metric": metric,
            "W statistic": round(statistic, 4),
            "p-value": p,
            "Normal": "Yes" if p > 0.05 else "No",
        })

# Save the normality test results.

normality_results = pd.DataFrame(normality_results)

normality_results["p-value"] = normality_results["p-value"].apply(
    lambda p: "<0.001" if p < 0.001 else f"{p:.4f}"
)

print(normality_results)

normality_results.to_csv(
    "/content/drive/MyDrive/Colab Notebooks/Shapiro_Wilk_Results.csv",
    index=False,
)

print("\nShapiro_Wilk_Results.csv saved successfully.")

========================================== Factorial Linear Model ========================================
# Load the individual tree LSP datasets.

import pandas as pd
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm

p = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Platanus_LSP_Tree.csv")
c = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Celtis_LSP_Tree.csv")
j = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Japonicum_LSP_Tree.csv")

# Add species labels.

p["Species"] = "Platanus"
c["Species"] = "Celtis"
j["Species"] = "Styphnolobium"

# Combine the datasets.

data = pd.concat([p, c, j], ignore_index=True)

data["Species"] = data["Species"].astype("category")
data["LST_zone"] = data["LST_zone"].astype("category")

metrics = ["SOS", "POS", "EOS", "GSL"]

anova_results = []

# Test the effects of species, thermal zone, and their interaction.

for metric in metrics:

    model = smf.ols(
        f"{metric} ~ C(Species) * C(LST_zone)",
        data=data,
    ).fit()

    anova = anova_lm(model, typ=2)

    print(f"\n{'=' * 70}")
    print(f"{metric} ANOVA")
    print("=" * 70)
    print(anova)

    for effect in anova.index:

        anova_results.append({
            "Metric": metric,
            "Effect": effect,
            "DF": anova.loc[effect, "df"],
            "F": anova.loc[effect, "F"],
            "P_value": anova.loc[effect, "PR(>F)"],
        })

# Save the ANOVA results.

anova_results = pd.DataFrame(anova_results)

anova_results["P_value"] = anova_results["P_value"].apply(
    lambda p: "<0.001" if p < 0.001 else round(p, 4)
)

print(anova_results)

anova_results.to_csv(
    "/content/drive/MyDrive/Colab Notebooks/Species_ThermalZone_ANOVA.csv",
    index=False,
)

print("\nSpecies_ThermalZone_ANOVA.csv saved successfully.")

========================================== Ploting Species Thermal Interaction ========================================
# Load the individual tree LSP datasets.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

p = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Platanus_LSP_Tree.csv")
c = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Celtis_LSP_Tree.csv")
j = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Japonicum_LSP_Tree.csv")

p["Species"] = r"$\it{Platanus\ \times\ hispanica}$"
c["Species"] = r"$\it{Celtis\ australis}$"
j["Species"] = r"$\it{Styphnolobium\ japonicum}$"

# Combine the datasets.

data = pd.concat([p, c, j], ignore_index=True)

data["Species"] = data["Species"].astype("category")
data["LST_zone"] = data["LST_zone"].astype("category")

metrics = ["SOS", "POS", "EOS", "GSL"]
titles = ["(a) SOS", "(b) POS", "(c) EOS", "(d) GSL"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes = axes.flatten()

# Plot the interaction between species and thermal zone.

for ax, metric, title in zip(axes, metrics, titles):

    model = smf.ols(
        f"{metric} ~ C(Species) * C(LST_zone)",
        data=data,
    ).fit()

    pred = pd.DataFrame({
        "Species": np.repeat(data["Species"].cat.categories, 2),
        "LST_zone": [1, 4] * 3,
    })

    pred["Species"] = pd.Categorical(
        pred["Species"],
        categories=data["Species"].cat.categories,
    )

    pred["LST_zone"] = pd.Categorical(
        pred["LST_zone"],
        categories=data["LST_zone"].cat.categories,
    )

    prediction = model.get_prediction(pred).summary_frame(alpha=0.05)

    pred["Mean"] = prediction["mean"]
    pred["Lower"] = prediction["mean_ci_lower"]
    pred["Upper"] = prediction["mean_ci_upper"]

    for i, species in enumerate(pred["Species"].cat.categories):

        tmp = pred[pred["Species"] == species]

        ax.errorbar(
            [1, 4],
            tmp["Mean"],
            yerr=[
                tmp["Mean"] - tmp["Lower"],
                tmp["Upper"] - tmp["Mean"],
            ],
            color=colors[i],
            linewidth=3,
            marker="o",
            markersize=8,
            capsize=4,
            label=species,
        )

    ax.set_title(title, fontsize=13)
    ax.set_xticks([1, 4])
    ax.set_xticklabels(["Zone 1", "Zone 4"])
    ax.set_xlabel("Thermal Zone", fontsize=12)
    ax.set_ylabel(metric, fontsize=12)
    ax.grid(alpha=0.15)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

# Add a common legend.

handles, labels = axes[0].get_legend_handles_labels()

fig.legend(
    handles,
    labels,
    loc="upper center",
    ncol=3,
    frameon=False,
    fontsize=11,
    bbox_to_anchor=(0.5, 1.02),
)

plt.tight_layout(rect=[0, 0, 1, 0.95])

plt.savefig(
    "/content/drive/MyDrive/Colab Notebooks/Interaction_Plot_Publication.png",
    dpi=600,
    bbox_inches="tight",
)

plt.show()

========================================== Factorial Linear Model Table ========================================
# Generate the publication-ready ANOVA table.

import pandas as pd
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm

metrics = ["SOS", "POS", "EOS", "GSL"]

results = []

for metric in metrics:

    model = smf.ols(
        f"{metric} ~ C(Species) * C(LST_zone)",
        data=data,
    ).fit()

    anova = anova_lm(model, typ=2)

    for effect in [
        "C(Species)",
        "C(LST_zone)",
        "C(Species):C(LST_zone)",
    ]:

        p = anova.loc[effect, "PR(>F)"]

        results.append({
            "LSP Metric": metric,
            "Effect": effect
                .replace("C(Species)", "Species")
                .replace("C(LST_zone)", "Thermal Zone")
                .replace(
                    "C(Species):C(LST_zone)",
                    "Species × Thermal Zone",
                ),
            "df": int(anova.loc[effect, "df"]),
            "F": round(anova.loc[effect, "F"], 2),
            "p-value": "<0.001" if p < 0.001 else f"{p:.3f}",
        })

# Save the ANOVA summary table.

results = pd.DataFrame(results)

print(results)

results.to_csv(
    "/content/drive/MyDrive/Colab Notebooks/Table4_Factorial_Model.csv",
    index=False,
)

print("\nTable4_Factorial_Model.csv saved successfully.")

