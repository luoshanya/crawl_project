# 安装Pillow pip install Pillow  直接引用  from PIL import Image

import pytesseract
from PIL import Image

#路径导入
pytesseract.pytesseract.tesseract_cmd = r'E:\carlow\tesseract\Tesseract-OCR\tesseract.exe'
#打开图片
img = Image.open('c.jpg')
#将图片转文本
text = pytesseract.image_to_string(img,lang='chi_sim')
print(text)