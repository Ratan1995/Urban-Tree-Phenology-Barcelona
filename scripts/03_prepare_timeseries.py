import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the LST datasets.

platanus = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Platanus_LST_4zones.csv")
celtis = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Celtis_LST_4zones.csv")
japonicum = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Japonicum_LST_4zones.csv")

datasets = [
    (r"(a) $\it{Platanus\ \times\ hispanica}$", platanus),
    (r"(b) $\it{Celtis\ australis}$", celtis),
    (r"(c) $\it{Styphnolobium\ japonicum}$", japonicum),
]

# Configure the publication-style figure.

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.linewidth": 1.2,
    "axes.labelsize": 14,
    "axes.titlesize": 15,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,
    "xtick.direction": "in",
    "ytick.direction": "in",
})

colors = [
    "#d95f02",
    "#fdb863",
    "#1b9e77",
    "#2c7fb8",
]

all_values = pd.concat([
    platanus["Mean_LST"],
    celtis["Mean_LST"],
    japonicum["Mean_LST"],
])

ymin = all_values.min() - 0.3
ymax = all_values.max() + 0.3

fig, axes = plt.subplots(
    1,
    3,
    figsize=(17, 6),
    sharey=True,
)

# Create the raincloud plots.

for ax, (title, df) in zip(axes, datasets):

    data = [
        df[df["LST_zone"] == 1]["Mean_LST"],
        df[df["LST_zone"] == 2]["Mean_LST"],
        df[df["LST_zone"] == 3]["Mean_LST"],
        df[df["LST_zone"] == 4]["Mean_LST"],
    ]

    vp = ax.violinplot(
        data,
        positions=[1, 2, 3, 4],
        widths=0.8,
        showmeans=False,
        showmedians=False,
        showextrema=False,
    )

    for body, color in zip(vp["bodies"], colors):
        body.set_facecolor(color)
        body.set_edgecolor("black")
        body.set_alpha(0.30)

    bp = ax.boxplot(
        data,
        positions=[1, 2, 3, 4],
        widths=0.25,
        patch_artist=True,
        showfliers=False,
    )

    for patch, color in zip(bp["boxes"], colors):
        patch.set_facecolor(color)
        patch.set_edgecolor("black")
        patch.set_linewidth(1.4)

    for median in bp["medians"]:
        median.set_color("black")
        median.set_linewidth(2)

    for whisker in bp["whiskers"]:
        whisker.set_linewidth(1.2)

    for cap in bp["caps"]:
        cap.set_linewidth(1.2)

    np.random.seed(42)

    for i, zone in enumerate([1, 2, 3, 4], start=1):

        y = df[df["LST_zone"] == zone]["Mean_LST"]
        x = np.random.normal(i, 0.045, len(y))

        ax.scatter(
            x,
            y,
            s=7,
            alpha=0.15,
            color=colors[i - 1],
            edgecolor="none",
            rasterized=True,
        )

    ax.set_title(
        title,
        fontsize=15,
        fontweight="normal",
        pad=10,
    )

    ax.set_xticks([1, 2, 3, 4])
    ax.set_xticklabels(["Zone 1", "Zone 2", "Zone 3", "Zone 4"])

    ax.grid(
        axis="y",
        linestyle="--",
        linewidth=0.6,
        alpha=0.12,
    )

    ax.set_ylim(ymin, ymax)

axes[0].set_ylabel(
    "Mean Land Surface Temperature (°C)",
    fontsize=15,
)

axes[1].set_xlabel(
    "Thermal Zone",
    fontsize=15,
    labelpad=16,
)

# Save the figure.

plt.subplots_adjust(
    left=0.07,
    right=0.995,
    top=0.90,
    bottom=0.13,
    wspace=0.06,
)

plt.savefig(
    "Raincloud_ThermalZones_Publication.png",
    dpi=600,
    bbox_inches="tight",
)

plt.show()
