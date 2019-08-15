import pytesseract
from PIL import Image
import time
#因为要用url保存图片 可以使用urllib的request
from urllib import request

#验证码图片的url
url = 'https://login.51job.com/ajax/verifycode.php?type=33&from_domain=i&t=1552556243553'
#导入tesseract的位置
# pytesseract.pytesseract.tesseract_cmd = r'E:\carlow\tesseract\Tesseract-OCR\tesseract.exe'
#因为验证码不一定准确，所以要一个死循环
# while True:
request.urlretrieve(url,'a1.jpg')
# #识别验证码
# img = Image.open('a1.jpg')
#图像转文本
# text = pytesseract.image_to_string(img)
# print(text)
#沉睡
# time.sleep(2)


