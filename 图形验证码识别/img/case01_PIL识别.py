import tesserocr
from PIL import Image


#20%左右的成功率
for i in range(1,5):
    str = 'code{}.jpg'.format(i)
    image = Image.open(str)
    #使用image_to_text()方法
    result = tesserocr.image_to_text(image).strip()
    print(result)