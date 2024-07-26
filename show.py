import os,cv2
import ultralytics
from ultralytics import YOLO
import matplotlib.pyplot as plt
from tesseractt import extract_text_from_image


def crop_img(path):
  im0 = cv2.imread(path)

  results = model.predict(im0)

  boxes = results[0].boxes.xyxy.cpu().numpy()
  clss = results[0].boxes.cls.cpu().tolist()

  print(boxes, clss)

  for i, box in enumerate(boxes):
      x1, y1, x2, y2 = map(int, box)  
      cropped_img = im0[y1:y2, x1:x2]  
      cv2.imshow(f"Cropped Image {i}", cropped_img)
      cv2.imshow("anh goc:", im0)
      print(extract_text_from_image(cropped_img))
      # cv2.imwrite(os.path.join(expected_path,name), cropped_img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

for image in os.listdir(r'F:/project/plate/makedataset/GreenParking_dataset/val/images'):
  path=os.path.join('F:/project/plate/makedataset/GreenParking_dataset/val/images', image)
  crop_img(path)
# for image in os.listdir(r'F:/project/plate/makedataset/GreenParking_dataset/val/images'):
#   results=model(f'F:/project/plate/makedataset/GreenParking_dataset/val/images/{image}')
#   for result in results:   
#     result.save(f'F:/project/plate/images_detect/{image}')

# for image in os.listdir('F:/project/plate/images_detect'):
#   if image.endswith('.jpg'):
#     img=plt.imread(f'F:/project/plate/images_detect/{image}')
    
#     print(image)
#     plt.imshow(img)
#     plt.axis('off')
#     plt.show()