import cv2
import numpy as np

# Load an image
image = cv2.imread('your_image.jpg')

# Convert the image to the HSV color space (Hue, Saturation, Value)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the lower and upper thresholds for the color you want to segment
lower_color = np.array([30, 50, 50])  # Lower threshold for blue color
upper_color = np.array([90, 255, 255])  # Upper threshold for blue color

# Create a binary mask where the pixels within the color range are set to 1 (white)
mask = cv2.inRange(hsv_image, lower_color, upper_color)

# Apply the mask to the original image
segmented_image = cv2.bitwise_and(image, image, mask=mask)

# Display the original image and the segmented image
cv2.imshow('Original Image', image)
cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
