import os
import glob
import numpy as np
import pandas as pd
import rasterio

# ==========================================================
# Input paths
# ==========================================================

image_folder = r"/content/drive/MyDrive/Colab Notebooks/EVI_Images"

species_files = [
    (
        "Platanus",
        r"/content/drive/MyDrive/Colab Notebooks/Platanus_LST_4zones.csv",
        r"/content/drive/MyDrive/Colab Notebooks/Platanus_EVI_Timeseries.csv",
    ),
    (
        "Celtis",
        r"/content/drive/MyDrive/Colab Notebooks/Celtis_LST_4zones.csv",
        r"/content/drive/MyDrive/Colab Notebooks/Celtis_EVI_Timeseries.csv",
    ),
    (
        "Japonicum",
        r"/content/drive/MyDrive/Colab Notebooks/Japonicum_LST_4zones.csv",
        r"/content/drive/MyDrive/Colab Notebooks/Japonicum_EVI_Timeseries.csv",
    ),
]

# ==========================================================
# Find all EVI images
# ==========================================================

image_files = sorted(glob.glob(os.path.join(image_folder, "*.tif")))

print(f"{len(image_files)} images found.")

# ==========================================================
# Extract the EVI time series
# ==========================================================

for species, input_csv, output_csv in species_files:

    print(f"\nProcessing {species}...")

    trees = pd.read_csv(input_csv)

    coordinates = list(
        zip(
            trees["x_etrs89"],
            trees["y_etrs89"]
        )
    )

    for image_path in image_files:

        image_name = os.path.splitext(
            os.path.basename(image_path)
        )[0]

        print(f"   {image_name}")

        with rasterio.open(image_path) as src:

            values = [
                value[0] if not np.isnan(value[0]) else np.nan
                for value in src.sample(coordinates)
            ]

        trees[image_name] = values

    trees.to_csv(output_csv, index=False)

    print(f"Saved: {output_csv}")

print("\nFinished processing all species.")
