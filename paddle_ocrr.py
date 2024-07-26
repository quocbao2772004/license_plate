from paddleocr import PaddleOCR,draw_ocr
ocr = PaddleOCR(use_angle_cls=True, lang='en')
def read_text_using_paddleocr(img):
    result = ocr.ocr(img, cls=True)
    text = result[0][0][1][0] +'\n'+ result[0][1][1][0]
    return text