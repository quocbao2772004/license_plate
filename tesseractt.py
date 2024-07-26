import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    binary = cv2.medianBlur(binary, 3)
    return binary

def extract_text_from_image(image):
    # processed_image = preprocess_image(image_path)
    # cv2.imwrite("processed_image.png", processed_image)
    # processed_image = cv2.imread(image_path)
    text = pytesseract.image_to_string(image, lang='eng', config=r'--oem 3 --psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') 
    # cv2.putText(image, text, (50, 50), cv2.FONT_HERSHEY_PLAIN, 3.0, (0, 0, 255), lineType=cv2.LINE_AA)
    # cv2.imshow("hihi",image)
    # cv2.waitKey(0)
    return text

# image_path = r"C:\users\pc\Pictures\screenshots\Screenshot 2024-07-19 132810.png"
# img=cv2.imread(image_path)
# print(extract_text_from_image(img))



