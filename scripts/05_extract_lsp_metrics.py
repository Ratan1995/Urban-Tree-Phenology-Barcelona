# Extract LSP metrics from the fitted curves.

lsp_results = []

for _, curve in curve_results.iterrows():
    species = curve["Species"]
    zone = curve["Zone"]
    days = np.array(curve["Smooth_Days"])
    y_smooth = np.array(curve["Smooth_EVI"])
    y = np.array(curve["Observed_EVI"])

    # Calculate the 20% dynamic threshold.
    evi_min = y_smooth.min()
    evi_max = y_smooth.max()
    threshold = evi_min + 0.20 * (evi_max - evi_min)

    pos_idx = np.argmax(y_smooth)
    sos_idx = np.where(y_smooth >= threshold)[0][0]
    eos_idx = np.where(y_smooth >= threshold)[0][-1]

    lsp_results.append({
        "Species": species,
        "Zone": zone,
        "SOS": days[sos_idx],
        "POS": days[pos_idx],
        "EOS": days[eos_idx],
        "LOS": days[eos_idx] - days[sos_idx],
        "Threshold": threshold,
        "Curve_Days": days,
        "Curve_EVI": y_smooth,
        "Observed_EVI": y,
        "SOS_Day": days[sos_idx],
        "SOS_EVI": y_smooth[sos_idx],
        "POS_Day": days[pos_idx],
        "POS_EVI": y_smooth[pos_idx],
        "EOS_Day": days[eos_idx],
        "EOS_EVI": y_smooth[eos_idx],
    })

lsp_results = pd.DataFrame(lsp_results)

print(lsp_results[["Species", "Zone", "SOS", "POS", "EOS", "LOS"]].round(2))


# Create the final LSP summary table.

from datetime import timedelta

first_date = pd.Timestamp("2024-02-01")
final_table = []

for _, row in lsp_results.iterrows():
    sos_date = first_date + timedelta(days=float(row["SOS"]))
    pos_date = first_date + timedelta(days=float(row["POS"]))
    eos_date = first_date + timedelta(days=float(row["EOS"]))

    final_table.append({
        "Species": row["Species"],
        "Zone": row["Zone"],
        "SOS_DOY": sos_date.dayofyear,
        "POS_DOY": pos_date.dayofyear,
        "EOS_DOY": eos_date.dayofyear,
        "LOS_days": round(row["LOS"], 1),
    })

final_table = pd.DataFrame(final_table)
print(final_table)


# Plot the extracted LSP metrics.

fig, axes = plt.subplots(1, 3, figsize=(18, 5), sharex=True, sharey=True)

for ax, (filepath, title) in zip(axes, files):
    species_data = lsp_results[lsp_results["Species"] == title]

    for _, row in species_data.iterrows():
        zone = row["Zone"]

        observed = curve_results[
            (curve_results["Species"] == title) &
            (curve_results["Zone"] == zone)
        ].iloc[0]

        ax.scatter(
            observed["Observed_Days"], row["Observed_EVI"],
            s=22, color=colors[zone], edgecolor="none",
            alpha=0.8, zorder=3
        )

        ax.plot(
            row["Curve_Days"], row["Curve_EVI"],
            color=colors[zone], linewidth=3,
            solid_capstyle="round", zorder=2
        )

        ax.scatter(row["SOS_Day"], row["SOS_EVI"], marker="o",
                   s=80, facecolors="white", edgecolors=colors[zone],
                   linewidth=2, zorder=6)

        ax.scatter(row["POS_Day"], row["POS_EVI"], marker="^",
                   s=100, color=colors[zone], edgecolor="black",
                   linewidth=0.4, zorder=6)

        ax.scatter(row["EOS_Day"], row["EOS_EVI"], marker="s",
                   s=80, facecolors="white", edgecolors=colors[zone],
                   linewidth=2, zorder=6)

    ax.set_title(title, fontsize=14, pad=8)
    ax.set_xlim(0, 365)
    ax.set_ylim(0.08, 0.42)
    ax.set_xticks([0, 50, 100, 150, 200, 250, 300, 350])
    ax.set_yticks(np.arange(0.10, 0.41, 0.05))
    ax.grid(False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

axes[0].set_ylabel("EVI", fontsize=13)
axes[1].set_xlabel("Day of Year (DOY)", fontsize=13)

legend = [
    Line2D([0], [0], color=colors[1], lw=3, label="Zone 1"),
    Line2D([0], [0], color=colors[4], lw=3, label="Zone 4"),
    Line2D([0], [0], marker="o", linestyle="None",
           markerfacecolor="white", markeredgecolor="black",
           markeredgewidth=1.5, markersize=8, label="SOS"),
    Line2D([0], [0], marker="^", linestyle="None",
           markerfacecolor="black", markeredgecolor="black",
           markersize=9, label="POS"),
    Line2D([0], [0], marker="s", linestyle="None",
           markerfacecolor="white", markeredgecolor="black",
           markeredgewidth=1.5, markersize=8, label="EOS"),
]

fig.legend(handles=legend, loc="upper center",
           bbox_to_anchor=(0.5, 1.05), ncol=5,
           frameon=True, edgecolor="black")

plt.tight_layout()
plt.show()


#Validation of LSP metrics

# ============================================================

validation = []

for _, row in lsp_results.iterrows():

    # Expected threshold
    threshold = row["Threshold"]

    # EVI at extracted SOS and EOS
    sos_evi = row["SOS_EVI"]
    eos_evi = row["EOS_EVI"]

    validation.append({

        "Species": row["Species"],

        "Zone": row["Zone"],

        "Threshold": threshold,

        "SOS_EVI": sos_evi,

        "EOS_EVI": eos_evi,

        "SOS_Error": abs(sos_evi - threshold),

        "EOS_Error": abs(eos_evi - threshold)

    })

validation = pd.DataFrame(validation)

print(validation.round(5))
