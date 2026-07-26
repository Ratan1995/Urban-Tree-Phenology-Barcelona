# Perform the sensitivity analysis.

import numpy as np
import pandas as pd

thresholds = [0.20, 0.25, 0.30]

sensitivity_results = []

for threshold_fraction in thresholds:

    for _, curve in curve_results.iterrows():

        species = curve["Species"]
        zone = curve["Zone"]

        days = np.array(curve["Smooth_Days"])
        y = np.array(curve["Smooth_EVI"])

        # Calculate the dynamic threshold.
        threshold = y.min() + threshold_fraction * (y.max() - y.min())

        sos_idx = np.where(y >= threshold)[0][0]
        pos_idx = np.argmax(y)
        eos_idx = np.where(y >= threshold)[0][-1]

        sensitivity_results.append({
            "Species": species,
            "Zone": zone,
            "Threshold": int(threshold_fraction * 100),
            "SOS": days[sos_idx],
            "POS": days[pos_idx],
            "EOS": days[eos_idx],
            "GSL": days[eos_idx] - days[sos_idx],
        })

# Save the sensitivity analysis results.

sensitivity_results = pd.DataFrame(sensitivity_results)

print(sensitivity_results)

sensitivity_results.to_csv(
    "/content/drive/MyDrive/Colab Notebooks/Sensitivity_LSP.csv",
    index=False,
)

print("\nSensitivity_LSP.csv saved successfully.")

# Calculate the sensitivity relative to the 20% threshold.

import pandas as pd

baseline = (
    sensitivity_results[sensitivity_results["Threshold"] == 20]
    .rename(columns={
        "SOS": "SOS20",
        "POS": "POS20",
        "EOS": "EOS20",
        "GSL": "GSL20",
    })
    [["Species", "Zone", "SOS20", "POS20", "EOS20", "GSL20"]]
)

comparison = sensitivity_results.merge(
    baseline,
    on=["Species", "Zone"],
)

# Calculate the absolute differences.

comparison["ΔSOS"] = abs(comparison["SOS"] - comparison["SOS20"])
comparison["ΔPOS"] = abs(comparison["POS"] - comparison["POS20"])
comparison["ΔEOS"] = abs(comparison["EOS"] - comparison["EOS20"])
comparison["ΔGSL"] = abs(comparison["GSL"] - comparison["GSL20"])

comparison = comparison[comparison["Threshold"] != 20]

# Summarize the sensitivity analysis.

summary = (
    comparison
    .groupby("Threshold")[["ΔSOS", "ΔPOS", "ΔEOS", "ΔGSL"]]
    .mean()
    .round(2)
)

print(summary)

summary.to_csv(
    "/content/drive/MyDrive/Colab Notebooks/Table5_Sensitivity.csv",
)

print("\nTable5_Sensitivity.csv saved successfully.")

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Prepare the sensitivity analysis data.

df = sensitivity_results.copy()

metrics = ["SOS", "POS", "EOS", "GSL"]
titles = ["(a) SOS", "(b) POS", "(c) EOS", "(d) GSL"]

species_order = list(df["Species"].unique())

colors = {
    species_order[0]: "#1f77b4",
    species_order[1]: "#ff7f0e",
    species_order[2]: "#2ca02c",
}

# Configure the publication-style figure.

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.labelsize": 13,
    "axes.titlesize": 14,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,
})

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

# Plot the sensitivity analysis.

for ax, metric, title in zip(axes, metrics, titles):

    for species in species_order:

        for zone in [1, 4]:

            tmp = (
                df[
                    (df["Species"] == species)
                    & (df["Zone"] == zone)
                ]
                .sort_values("Threshold")
            )

            ax.plot(
                tmp["Threshold"],
                tmp[metric],
                color=colors[species],
                linestyle="-" if zone == 1 else "--",
                linewidth=2.0,
                marker="o",
                markersize=4.2,
                markeredgewidth=0.7,
            )

    ax.set_title(title, pad=10, fontweight="bold")
    ax.set_xticks([20, 25, 30])

    ax.set_xlabel(
        "Dynamic threshold (%)"
        if metric in ["EOS", "GSL"]
        else ""
    )

    ax.set_ylabel(
        "GSL (days)"
        if metric == "GSL"
        else f"{metric} (DOY)"
    )

    ax.grid(
        linestyle="--",
        linewidth=0.6,
        alpha=0.18,
    )

    ax.set_axisbelow(True)
    ax.margins(y=0.08)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_linewidth(1.2)
    ax.spines["bottom"].set_linewidth(1.2)

# Add the figure legend.

legend_handles = [
    Line2D(
        [0], [0],
        color="#1f77b4",
        lw=2.2,
        label=r"$\it{Platanus\ \times\ hispanica}$",
    ),
    Line2D(
        [0], [0],
        color="#ff7f0e",
        lw=2.2,
        label=r"$\it{Celtis\ australis}$",
    ),
    Line2D(
        [0], [0],
        color="#2ca02c",
        lw=2.2,
        label=r"$\it{Styphnolobium\ japonicum}$",
    ),
    Line2D(
        [0], [0],
        color="black",
        lw=2,
        linestyle="-",
        label="Zone 1",
    ),
    Line2D(
        [0], [0],
        color="black",
        lw=2,
        linestyle="--",
        label="Zone 4",
    ),
]

fig.legend(
    handles=legend_handles,
    loc="upper center",
    bbox_to_anchor=(0.5, 1.02),
    ncol=5,
    frameon=False,
    fontsize=10,
    handlelength=2.2,
    columnspacing=1.6,
)

# Save the figure.

plt.subplots_adjust(
    top=0.88,
    bottom=0.09,
    left=0.08,
    right=0.98,
    hspace=0.28,
    wspace=0.25,
)

plt.savefig(
    "Figure9_Final_Publication.png",
    dpi=600,
    bbox_inches="tight",
)

plt.show()

