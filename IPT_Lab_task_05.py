# %% [markdown]
# Task No. 1
#
# Question:
# Apply Global Histogram Equalization (equalizeHist) and Adaptive Histogram Equalization (CLAHE) to the same grayscale image. Test clipLimit values 1, 2, and 4, and compare tileGridSize values 8x8 and 16x16.

# %%
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import data

print("OpenCV version:", cv2.__version__)

# %%
img = data.camera()

print("Image shape:", img.shape)
print("Image data type:", img.dtype)
print("Minimum intensity:", img.min())
print("Maximum intensity:", img.max())

plt.figure(figsize=(6, 5))
plt.imshow(img, cmap="gray", vmin=0, vmax=255)
plt.title("Original Grayscale Image")
plt.axis("off")
plt.show()

# %%
global_eq = cv2.equalizeHist(img)

fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].imshow(global_eq, cmap="gray", vmin=0, vmax=255)
ax[0].set_title("Global Equalization (equalizeHist)")
ax[0].axis("off")
ax[1].hist(global_eq.ravel(), bins=256, range=(0, 256))
ax[1].set_title("Histogram after Global Equalization")
ax[1].set_xlim(0, 255)
ax[1].set_xlabel("Pixel intensity")
ax[1].set_ylabel("Number of pixels")
plt.tight_layout()
plt.show()

# %%
clip_limits = [1.0, 2.0, 4.0]
clahe_8 = {}

fig, axes = plt.subplots(2, 3, figsize=(14, 8))
for i, limit in enumerate(clip_limits):
    clahe = cv2.createCLAHE(clipLimit=limit, tileGridSize=(8, 8))
    result = clahe.apply(img)
    clahe_8[limit] = result

    axes[0, i].imshow(result, cmap="gray", vmin=0, vmax=255)
    axes[0, i].set_title(f"CLAHE: clipLimit={limit}, tiles=8x8")
    axes[0, i].axis("off")

    axes[1, i].hist(result.ravel(), bins=256, range=(0, 256))
    axes[1, i].set_title(f"Histogram (clipLimit={limit})")
    axes[1, i].set_xlim(0, 255)
    axes[1, i].set_xlabel("Intensity")

plt.tight_layout()
plt.show()

# %%
tile_sizes = [(8, 8), (16, 16)]
clahe_tiles = {}

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
for ax, tile_size in zip(axes, tile_sizes):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=tile_size)
    result = clahe.apply(img)
    clahe_tiles[tile_size] = result

    ax.imshow(result, cmap="gray", vmin=0, vmax=255)
    ax.set_title(
        f"CLAHE: clipLimit=2, tiles={tile_size[0]}x{tile_size[1]}"
    )
    ax.axis("off")

plt.tight_layout()
plt.show()

# %%
comparison_images = [
    (img, "Original"),
    (global_eq, "Global equalization"),
    (clahe_8[1.0], "CLAHE clipLimit=1"),
    (clahe_8[2.0], "CLAHE clipLimit=2"),
    (clahe_8[4.0], "CLAHE clipLimit=4"),
    (clahe_tiles[(16, 16)], "CLAHE tiles=16x16"),
]

fig, axes = plt.subplots(2, 3, figsize=(13, 8))
for ax, (image, title) in zip(axes.ravel(), comparison_images):
    ax.imshow(image, cmap="gray", vmin=0, vmax=255)
    ax.set_title(title)
    ax.axis("off")

plt.tight_layout()
plt.show()

# %%
print("OBSERVATIONS")
print("1. Global equalization improves overall contrast using the whole image histogram.")
print("2. CLAHE with clipLimit 1 gives gentle enhancement and often looks natural.")
print("3. CLAHE with clipLimit 2 gives a useful balance between detail and contrast.")
print("4. CLAHE with clipLimit 4 enhances local contrast more strongly; texture and noise may become more visible.")
print("5. A tile size of 8x8 adjusts contrast in smaller regions, while 16x16 uses larger regions and may look smoother.")
