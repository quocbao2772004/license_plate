import cv2
import torch,os
from ultralytics import YOLO
from tesseractt import extract_text_from_image
model = YOLO(r'F:\project\plate\model\plate.pt')
def crop_img_and_show_plate(path):
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

# crop_img(r"C:\Users\PC\Downloads\Screenshot 2024-07-16 205829.png", r"C:\Users\PC\Downloads" , "thu.png")
def crop_img(path):
  im0 = cv2.imread(path)

  results = model.predict(im0)

  boxes = results[0].boxes.xyxy.cpu().numpy()
  clss = results[0].boxes.cls.cpu().tolist()

  # print(boxes, clss)

  for i, box in enumerate(boxes):
      x1, y1, x2, y2 = map(int, box)  
      cropped_img = im0[y1:y2, x1:x2]  
      cv2.imshow(f"Cropped Image {i}", cropped_img)
      cv2.imshow("anh goc:", im0)
      print(extract_text_from_image(cropped_img))
      # cv2.imwrite(os.path.join(expected_path,name), cropped_img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()