import ultralytics, os, cv2 
from ultralytics import YOLO
from put_text import put_text_with_pillow
from paddle_ocrr import read_text_using_paddleocr, read_text_using_paddleocr_part_2
from tesseractt import preprocess_image, extract_text_from_image
from processing import tao_nen, show_lisence_plate

from ultralytics.utils.plotting import Annotator, colors
import matplotlib.pyplot as plt

font_size = 18
color = (178 ,34, 34)
color_rec=(178 ,34, 34)
font_path = r"/home/quoc-bao/Downloads/Bo-Font-Full/Bo-Font-tieng-Trung-Quoc/Bộ Font tiếng Trung Quốc/14-bo-font-tieng-trung-dac-biet- chinesecomvn/fzstk.ttf"
model = YOLO(r'/home/quoc-bao/code/Lisence_plate/license_plate/model/plate2.pt')

def crop_img_and_show_plate(im0):
            results = model.predict(im0)
            boxes = results[0].boxes.xyxy.cpu().numpy()
            clss = results[0].boxes.cls.cpu().tolist()
            for i, box in enumerate(boxes):
                x1, y1, x2, y2 = map(int, box)
                cropped_img = im0[y1:y2, x1:x2]
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
            img_putted_text = put_text_with_pillow(img, text, position_number, font_path, font_size, color)
            
            cv2.imshow("Show", img_putted_text)
            cv2.waitKey(0)
        else:
            cv2.imshow("Show", im0)
        
def video():

    video_path = r"F:\project\plate\makedataset\bike_counter_10min.mp4"
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():

        success, frame = cap.read()
        if success:
            frame = cv2.resize(frame, (640, 480))
            results = model.track(frame, persist=True)
            annotated_frame = results[0].plot()
            cv2.imshow("show", frame)

            if results[0].boxes:
                for box in results[0].boxes.xyxy:
                    x1, y1, x2, y2 = map(int, box[:4])
                    cropped_img = frame[y1:y2, x1:x2]
                    
                    text = return_result(cropped_img)
                    print(text)
                    # cv2.imshow("Cropped Image", cropped_img)
                    # cv2.imwrite(f'cropped_{x1}_{y1}.png', cropped_img)

            if cv2.waitKey(10) & 0xFF == ord("q"):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
       
def main():
    image()
    
if __name__ == '__main__':
    main()
