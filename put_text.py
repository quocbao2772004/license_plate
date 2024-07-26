from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np

def put_text_with_pillow(img, text, position, font_path, font_size, color):
    
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype(font_path, font_size)

    draw.text(position, text, font=font, fill=color)
    
    img = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
    return img

# # Ví dụ sử dụng
# img = cv2.imread(r"C:\Users\PC\Downloads\xe1_cropped.png")
# text = extract_text_from_image(img)

# # for t in text:
# #     print(t)
# position = (50, 50)
# font_path = r"C:\Windows\WinSxS\Temp\InFlight\ec74b6947443da01970500001846a06b\amd64_microsoft-windows-font-truetype-segoeui_31bf3856ad364e35_10.0.22621.2361_none_b0b27ccc8dc6166c\seguisym.ttf"  # Đường dẫn tới tệp font TrueType
# font_size = 30
# color = (255, 0, 0)  # Màu đỏ (R, G, B)
# img2=cv2.imread(r"C:\Users\PC\Downloads\Screenshot 2024-07-16 205829.png")
# img_with_text = put_text_with_pillow(img2, text, position, font_path, font_size, color)

# cv2.imshow("Image with Text", img_with_text)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
