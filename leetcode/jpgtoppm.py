import cv2
import numpy as np
# Load the image
image = cv2.imread('image.png')

# Convert the image to a NumPy array
image_array = np.array(image)

print(image_array)