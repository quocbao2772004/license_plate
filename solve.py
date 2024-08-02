import ultralytics, os, cv2 
from ultralytics import YOLO
from put_text import put_text_with_pillow
from paddle_ocrr import read_text_using_paddleocr, read_text_using_paddleocr_part_2
from tesseractt import preprocess_image, extract_text_from_image
from processing import show_lisence_plate
import time
from ultralytics.utils.plotting import Annotator, colors
import matplotlib.pyplot as plt

font_size = 18
color = (178 ,34, 34)
color_rec=(178 ,34, 34)
font_path = r"/home/quoc-bao/Downloads/Bo-Font-Full/Bo-Font-tieng-Trung-Quoc/Bộ Font tiếng Trung Quốc/14-bo-font-tieng-trung-dac-biet- chinesecomvn/fzstk.ttf"
model = YOLO(r'/home/quoc-bao/code/Lisence_plate/license_plate/model/plate2.pt')

def create_paddingg(original_image):
    if original_image is None:
        print("Error: Could not read the image.")
        return None
    else:
        
        height, width, channels = original_image.shape
        top_padding = 10
        bottom_padding = 10
        left_padding = 10
        right_padding = 10
        
        padded_image = cv2.copyMakeBorder(
            original_image,
            top_padding, bottom_padding, left_padding, right_padding,
            borderType=cv2.BORDER_CONSTANT,
            value=[0, 0, 0]  
        )
        
        return padded_image
    
def crop_img_and_show_plate(im0):
            results = model.predict(im0)
            boxes = results[0].boxes.xyxy.cpu().numpy()
            clss = results[0].boxes.cls.cpu().tolist()
            for i, box in enumerate(boxes):
                x1, y1, x2, y2 = map(int, box)
                cropped_img = im0[y1:y2, x1:x2]
                cropped_img = create_paddingg(cropped_img)
                text=read_text_using_paddleocr(cropped_img)
                if text == "":
                    text = read_text_using_paddleocr_part_2(im0)
                if text == "":
                    text = "Error"
                return 1,text,x1,y1,x2,y2
            return 0,None, None, None, None, None
        
def image():
    data1='/home/quoc-bao/code/Lisence_plate/license_plate/makedataset/GreenParking'
    data2='/home/quoc-bao/code/easy_ocr/CarTGMT'
    for image in os.listdir(data2):
        print(image)
        start_time=time.time()
        path=os.path.join(data2, image)
        im0=cv2.imread(path)
        status, text, x1, y1, x2, y2 = crop_img_and_show_plate(im0)
        if status:
            
            print(text)
            img=cv2.imread(path)
            height, width = im0.shape[:2]
            position_number = (width+2, height//2 + 20)

            cv2.rectangle(img, (x1, y1), (x2, y2), color_rec, 2)
            img=show_lisence_plate(img, img[y1:y2,x1:x2])
            end_time=time.time()
            total_time=end_time-start_time
            img_putted_text = put_text_with_pillow(img, text, position_number, font_path, font_size, color)
            img_putted_text = put_text_with_pillow(img_putted_text, str(total_time), (width+2,height//1.1), font_path, font_size, color)
            # print(total_time)
            cv2.imshow("Show", img_putted_text)
            cv2.waitKey(0)
            
        else:
            cv2.imshow("Show", im0)
        
        
            
def main():
    image()
    
if __name__ == '__main__':
    main()
