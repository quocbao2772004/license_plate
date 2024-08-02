from paddleocr import PaddleOCR,draw_ocr
import cv2

def check_number(i):
    if i>='0' and i<='9':
        return 1
    return 0

def check_alpha(i):
    if i>='A' and i<='Z':
        return 1
    return 0

ocr = PaddleOCR(use_angle_cls=True, lang='en')
def read_text_using_paddleocr(img):
    result = ocr.ocr(img, cls=True)
    if len(result)==0 or str(result)=='[None]':
        return ""
    elif len(result[0])>=2:
        text = result[0][0][1][0] +'\n'+ result[0][1][1][0]
    else:
        text = result[0][0][1][0]
    return text

def read_text_using_paddleocr_part_2(img):
    result = ocr.ocr(img, cls=True)
    text = result
    res=""
    for i in range(0,len(text[0])):
        
        t=text[0][i][1][0]
        if (check_number(t[0]) and check_number(t[1]) and check_alpha(t[2])):
            res+=t
        elif t.find('.')!=-1 and (len(t)==4 or len(t)==5 or len(t)==6):
            res=res+"\n"+t
    return res
    

# print(read_text_using_paddleocr_part_2(cv2.imread('/home/quoc-bao/code/easy_ocr/CarTGMT/license_plate_0062.jpg')))
