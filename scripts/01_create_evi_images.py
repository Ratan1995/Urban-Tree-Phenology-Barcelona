import glob
import os

import numpy as np
import rasterio

# Input and output folders.

input_folder = r"/content/drive/MyDrive/Colab Notebooks/PlanetScope_Images"
output_folder = r"/content/drive/MyDrive/Colab Notebooks/EVI_Images"

os.makedirs(output_folder, exist_ok=True)

image_files = sorted(glob.glob(os.path.join(input_folder, "*.tif")))

print(f"{len(image_files)} images found.")

# Calculate EVI for each PlanetScope image.

for image_path in image_files:

    image_name = os.path.basename(image_path)

    print(f"Processing: {image_name}")

    with rasterio.open(image_path) as src:

        profile = src.profile.copy()

        # PlanetScope SuperDove bands
        blue = src.read(2).astype(np.float32)
        red = src.read(6).astype(np.float32)
        nir = src.read(8).astype(np.float32)

        # Convert DN to reflectance
        blue /= 10000.0
        red /= 10000.0
        nir /= 10000.0

        denominator = nir + 6 * red - 7.5 * blue + 1.0

        evi = np.where(
            denominator != 0,
            2.5 * (nir - red) / denominator,
            np.nan,
        )

        profile.update(
            dtype=rasterio.float32,
            count=1,
            nodata=np.nan,
        )

        output_path = os.path.join(output_folder, image_name)

        with rasterio.open(output_path, "w", **profile) as dst:
            dst.write(evi.astype(np.float32), 1)

print("\nFinished creating EVI images.")
