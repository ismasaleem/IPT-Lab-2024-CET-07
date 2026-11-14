# %% [markdown]
# Lab 03 – IPT
# Tasks I to IV

# %%
import numpy as np
import cv2
from google.colab.patches import cv2_imshow

# %% [markdown]
# ## Task I: NumPy Array, Sum and Average

# %%
numbers = np.array([5, 10, 15])
total = np.sum(numbers)
average = np.mean(numbers)
print("Array:", numbers)
print("Sum:", total)
print("Average:", average)

"""
Array: [ 5 10 15]
Sum: 30
Average: 10.0
"""

# %% [markdown]
# ## Task II: Change the Text Message

# %%
message = "Hello! This is my image."
print("Message:", message)

"""
Message: Hello! This is my image.
"""

# %% [markdown]
# ## Task III: Resize Image Dimensions

# %%
original_image = np.zeros((300, 400, 3), dtype=np.uint8)
print("Original image shape:", original_image.shape)
resized_image = cv2.resize(original_image, (500, 200))
print("Resized image shape:", resized_image.shape)

"""
Original image shape: (300, 400, 3)
Resized image shape: (200, 500, 3)
"""

# %% [markdown]
# ## Task IV: Add Red Text and Display Final Image

# %%
red = (0, 0, 255)  # Red colour in OpenCV BGR format
cv2.putText(resized_image, message, (15, 110),
            cv2.FONT_HERSHEY_SIMPLEX, 0.65, red, 2, cv2.LINE_AA)
cv2.imwrite("lab03_tasks_output.png", resized_image)
print("Message:", message)
print("Text colour (BGR):", red)
print("Output image saved as: lab03_tasks_output.png")
cv2_imshow(resized_image)

"""
Message: Hello! This is my image.
Text colour (BGR): (0, 0, 255)
Output image saved as: lab03_tasks_output.png
"""
