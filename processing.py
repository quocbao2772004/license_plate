import numpy as np
def tao_nen(original_image):
  if original_image is None:
      print("Error: Could not read the image.")
  else:
      height, width, channels = original_image.shape
      white_width = 100
      white_image = np.ones((height, white_width, channels), np.uint8) * 255
      combined_image = np.hstack((original_image, white_image))
      return combined_image