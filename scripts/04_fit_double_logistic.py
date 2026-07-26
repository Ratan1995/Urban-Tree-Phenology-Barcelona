# ============================================================
# PART 1
# Publication-quality Double Logistic Curves
# Three Species
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit
from matplotlib.lines import Line2D

# ============================================================
# Publication Settings
# ============================================================

plt.rcParams.update({

    "font.family": "DejaVu Sans",      # Set the writing format

    "font.size": 11,

    "axes.labelsize": 14,

    "axes.titlesize": 15,

    "axes.linewidth": 1.2,

    "xtick.labelsize": 11,

    "ytick.labelsize": 11,

    "legend.fontsize": 11,

    "xtick.direction": "in",

    "ytick.direction": "in"

})

# ============================================================
# File paths
# ============================================================

files = [

    (
        "/content/drive/MyDrive/Colab Notebooks/Platanus_EVI_Timeseries.csv",
        r"(a) $\it{Platanus\ \times\ hispanica}$"
    ),

    (
        "/content/drive/MyDrive/Colab Notebooks/Celtis_EVI_Timeseries.csv",
        r"(b) $\it{Celtis\ australis}$"
    ),

    (
        "/content/drive/MyDrive/Colab Notebooks/Journal/Japonicum_EVI_Timeseries.csv",
        r"(c) $\it{Styphnolobium\ japonicum}$"
    )

]

# ============================================================
# Publication colours
# ============================================================

colors = {

    1: "#d95f02",      # Zone 1

    4: "#2c7fb8"       # Zone 4

}

# ============================================================
# Helper function
# Automatically detect EVI columns
# ============================================================

def load_species(filepath):

    df = pd.read_csv(filepath)

    # ------------------------------------
    # Find all date columns automatically
    # ------------------------------------

    evi_columns = [

        col

        for col in df.columns

        if str(col).isdigit()

    ]

    grouped = (

        df

        .groupby("LST_zone")[evi_columns]

        .mean()

        .loc[[1,4]]

    )

    dates = pd.to_datetime(

        evi_columns,

        format="%Y%m%d"

    )

    t = (

        (dates - dates.min()).days.values

        / 365.0

    )

    return grouped, t

# ============================================================
# Determine common y-axis
# ============================================================

global_min = 999

global_max = -999

for filepath, _ in files:

    grouped, _ = load_species(filepath)

    ymin = np.nanmin(grouped.values)

    ymax = np.nanmax(grouped.values)

    global_min = min(global_min, ymin)

    global_max = max(global_max, ymax)

global_min -= 0.03

global_max += 0.03
# ============================================================
# PART 2
# Double Logistic Model
# ============================================================

def double_logistic(t, w, m, S, A, k1, k2):

    spring = 1.0 / (1.0 + np.exp(-k1 * (t - S)))

    autumn = 1.0 / (1.0 + np.exp(k2 * (t - A)))

    return w + (m - w) * (spring + autumn - 1.0)


# ============================================================
# Robust Double Logistic Curve Fitting
# ============================================================

def fit_double_logistic(t, y):

    y = np.asarray(y, dtype=np.float64)

    # ----------------------------------------
    # Remove missing values
    # ----------------------------------------

    valid = np.isfinite(y)

    t_fit = t[valid]

    y_fit = y[valid]

    # ----------------------------------------
    # Initial parameter guess
    # ----------------------------------------

    p0 = [

        np.min(y_fit),

        np.max(y_fit),

        0.25,

        0.75,

        20,

        20

    ]

    lower = [

        0.00,

        0.05,

        0.05,

        0.40,

        1,

        1

    ]

    upper = [

        0.60,

        0.90,

        0.50,

        1.10,

        100,

        100

    ]

    # ----------------------------------------
    # First fitting
    # ----------------------------------------

    params, _ = curve_fit(

        double_logistic,

        t_fit,

        y_fit,

        p0=p0,

        bounds=(lower, upper),

        maxfev=50000

    )

    # ----------------------------------------
    # Robust weighted fitting
    # ----------------------------------------

    residuals = y_fit - double_logistic(t_fit, *params)

    sigma = np.abs(residuals) + 0.003

    params, _ = curve_fit(

        double_logistic,

        t_fit,

        y_fit,

        p0=params,

        sigma=sigma,

        absolute_sigma=False,

        bounds=(lower, upper),

        maxfev=50000

    )

    return params


# ============================================================
# Smooth Curve
# ============================================================

def create_smooth_curve(params, t):

    t_smooth = np.linspace(

        t.min(),

        t.max(),

        1000

    )

    y_smooth = double_logistic(

        t_smooth,

        *params

    )

    return t_smooth, y_smooth
# ============================================================
# PART 3
# Plot Each Species (Updated Version)
# ============================================================

fig, axes = plt.subplots(

    nrows=1,

    ncols=3,

    figsize=(18,4.8),

    sharex=True,

    sharey=True

)
curve_results = []
for ax, (filepath, title) in zip(axes, files):

    # ========================================================
    # Load species data
    # ========================================================

    grouped, t = load_species(filepath)

    # ========================================================
    # Smooth curve
    # ========================================================

    t_smooth = np.linspace(

        0,

        1,

        1200

    )

    # ========================================================
    # Plot Zone 1 and Zone 4
    # ========================================================

    for zone in [1,4]:

        y = grouped.loc[zone].values.astype(float)

        params = fit_double_logistic(t, y)

        y_smooth = double_logistic(

            t_smooth,

            *params

        )
        curve_results.append({

            "Species": title,
            "Zone": zone,
            "Observed_Days": t * 365,
            "Observed_EVI": y,
            "Smooth_Days": t_smooth * 365,
            "Smooth_EVI": y_smooth,
             "Parameters": params

        })



        # ------------------------------------------
        # Observed EVI
        # ------------------------------------------

        ax.scatter(

            t*365,

            y,

            s=30,

            color=colors[zone],

            edgecolor="none",

            alpha=0.80,

            zorder=3

        )

        # ------------------------------------------
        # Double Logistic Curve
        # ------------------------------------------

        ax.plot(

            t_smooth*365,

            y_smooth,

            color=colors[zone],

            linewidth=3.0,

            solid_capstyle="round",

            zorder=2

        )

    # ========================================================
    # Legend (only first subplot)
    # ========================================================

      # ========================================================
    # Legend (Only in Japonicum panel)
    # ========================================================

    if ax == axes[2]:

        legend_elements = [

            # Zone 1
            Line2D(
                [0], [0],
                marker='o',
                linestyle='None',
                markerfacecolor=colors[1],
                markeredgecolor='none',
                markersize=6,
                label='Zone 1'
            ),

            # Zone 4
            Line2D(
                [0], [0],
                marker='o',
                linestyle='None',
                markerfacecolor=colors[4],
                markeredgecolor='none',
                markersize=6,
                label='Zone 4'
            ),

            # Double Logistic Curve
            Line2D(
                [0], [0],
                color='black',
                linewidth=3,
                label='Double logistic fit'
            )

        ]

        ax.legend(

            handles=legend_elements,

            loc="upper right",

            bbox_to_anchor=(0.98, 0.98),

            fontsize=10,

            frameon=True,

            facecolor="white",

            edgecolor="black",

            framealpha=1,

            fancybox=False,

            handlelength=2.5,

            handletextpad=0.8,

            borderpad=0.5,

            labelspacing=0.5

        )
    # ========================================================
    # Formatting
    # ========================================================

    ax.set_title(

        title,

        fontsize=14,

        fontweight="normal",

        pad=8

    )

    ax.set_xlim(

        0,

        365

    )

    ax.set_ylim(

        0.08,

        0.42

    )

    ax.set_xticks(

        [0,50,100,150,200,250,300,350]

    )

    ax.set_yticks(

        np.arange(0.10,0.41,0.05)

    )

    ax.tick_params(

        axis="both",

        width=1.1,

        length=4,

        labelsize=11

    )

    ax.grid(

        linestyle="--",

        linewidth=0.5,

        alpha=0.12

    )

    ax.spines["top"].set_visible(False)

    ax.spines["right"].set_visible(False)

# ============================================================
# Common Labels
# ============================================================

axes[0].set_ylabel(

    "EVI",

    fontsize=13,

    fontweight="normal"

)

axes[1].set_xlabel(

    "Day of Year (DOY)",

    fontsize=13,

    fontweight="normal",

    labelpad=10

)
# ============================================================
# Save fitted curves
# ============================================================

curve_results = pd.DataFrame(curve_results)

print(type(curve_results))
print(curve_results.head())
