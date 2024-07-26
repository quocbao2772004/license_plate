import ultralytics, os, cv2 
from ultralytics import YOLO
from put_text import put_text_with_pillow
from paddle_ocrr import read_text_using_paddleocr
from tesseractt import preprocess_image, extract_text_from_image
from processing import tao_nen
from check import check_plate
from ultralytics.utils.plotting import Annotator, colors
import matplotlib.pyplot as plt

font_size = 20
color = (178 ,34, 34)
color_rec=(16,54,103)
font_path = r"C:\Users\PC\Downloads\font ttf tiếng việt\2BYTE\VBODONP.TTF"

def image():
    model = YOLO(r'F:\project\plate\model\plate.pt')
    def crop_img_and_show_plate(path):
    
            im0 = cv2.imread(path)
            results = model.predict(im0)
            boxes = results[0].boxes.xyxy.cpu().numpy()
            clss = results[0].boxes.cls.cpu().tolist()
            for i, box in enumerate(boxes):
                x1, y1, x2, y2 = map(int, box)
                cropped_img = im0[y1:y2, x1:x2]
                text=read_text_using_paddleocr(cropped_img)
                return text,x1,y1,x2,y2
            return None, None, None, None, None 

    for image in os.listdir(r'C:\Users\PC\Desktop\makedataset\GreenParking\GreenParking'):
        path=os.path.join(r'C:\Users\PC\Desktop\makedataset\GreenParking\GreenParking', image)
        text, x1, y1, x2, y2 = crop_img_and_show_plate(path)

        print(text)
        img=cv2.imread(path)
        position = (480,10)

        cv2.rectangle(img, (x1, y1), (x2, y2), color_rec, 2)
        img=tao_nen(img)
        img_putted_text = put_text_with_pillow(img, text, position, font_path, font_size, color)
        cv2.imshow("Show", img_putted_text)
        cv2.waitKey(0)
        
def video():
    model = YOLO(r'F:\project\plate\model\plate3.pt')
    video_path = r"C:\Users\PC\Downloads\videoplayback.mp4"
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():

        success, frame = cap.read()
        if success:
            results = model.track(frame, persist=True)
            annotated_frame = results[0].plot()
            resized_frame = cv2.resize(annotated_frame, (640, 480))
            cv2.imshow(resized_frame)

            if results[0].boxes:
                for box in results[0].boxes.xyxy:
                    x1, y1, x2, y2 = map(int, box[:4])
                    cropped_img = frame[y1:y2, x1:x2]

                    text = read_text_using_paddleocr(cropped_img)
                    print(text)
                    # cv2.imshow("Cropped Image", cropped_img)
                    # cv2.imwrite(f'cropped_{x1}_{y1}.png', cropped_img)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
       
def main():
    image()
    # video()
if __name__ == '__main__':
    main()
