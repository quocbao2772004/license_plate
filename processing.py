import numpy as np
import cv2
from put_text import put_text_with_pillow

font_size = 20
color = (0 ,0, 0)
font_path = r"/home/quoc-bao/Downloads/Bo-Font-Full/Bo-Font-tieng-Trung-Quoc/Bộ Font tiếng Trung Quốc/14-bo-font-tieng-trung-dac-biet- chinesecomvn/fzstk.ttf"

def tao_nen(original_image):
  if original_image is None:
      print("Error: Could not read the image.")
  else:
      height, width, channels = original_image.shape
      white_width = 100
      white_image = np.ones((height, white_width, channels), np.uint8) * 255
      combined_image = np.hstack((original_image, white_image))
      return combined_image


def show_lisence_plate(image1, image2):
    height1, width1 = image1.shape[:2]
    height2, width2 = image2.shape[:2]

    max_height = max(height1, height2)
    max_width = max(width1, width2)
    w = min(width1, width2)+ 20*2
    r,l=0,0
    if w < 120:
        r,l = 35, 35
    else:
        r,l=20,20
    if height1 < max_height:
        image1 = cv2.copyMakeBorder(image1, 60, max_height-height1-60, r, l, cv2.BORDER_CONSTANT, value=[255, 255, 255])
        horizontal_concat = np.concatenate((image2, image1), axis=1)
    if height2 < max_height:
        image2 = cv2.copyMakeBorder(image2, 60, max_height-height2-60, r, l, cv2.BORDER_CONSTANT, value=[255, 255, 255])
        horizontal_concat = np.concatenate((image1, image2), axis=1)
    width, height = max(width1, width2)+2, max(height1,height2)//2 + 20
    rotate = (width, 0)
    # (min(max(height1, height2),max(width1,width2))+2,max(max(height1, height2)//2,0))
    horizontal_concat = put_text_with_pillow(horizontal_concat,"License"+"\n"+"Plate" , rotate, font_path, font_size, color)
    horizontal_concat = put_text_with_pillow(horizontal_concat,"Number" , (width, height//1.2), font_path, font_size, color)
    return horizontal_concat
    

