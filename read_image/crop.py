import cv2
import torch
from ultralytics import YOLO

# Tải mô hình YOLO đã huấn luyện
model = YOLO(r'F:\project\plate\read_image\plate.pt')

# Đọc ảnh
im0 = cv2.imread(r"C:\Users\PC\Downloads\xe2.jpg")

# Dự đoán các bounding boxes
results = model.predict(im0)

# Lấy các bounding boxes và các class
boxes = results[0].boxes.xyxy.cpu().numpy()
clss = results[0].boxes.cls.cpu().tolist()

# In ra các tọa độ bounding boxes và các class
print(boxes, clss)

# Lặp qua từng bounding box và crop ảnh
for i, box in enumerate(boxes):
    x1, y1, x2, y2 = map(int, box)  # Chuyển tọa độ sang số nguyên
    cropped_img = im0[y1:y2, x1:x2]  # Crop ảnh

    # Hiển thị ảnh đã crop
    cv2.imshow(f"Cropped Image {i}", cropped_img)

# Đợi cho đến khi nhấn phím bất kỳ để đóng tất cả các cửa sổ hiển thị ảnh
cv2.waitKey(0)
cv2.destroyAllWindows()
