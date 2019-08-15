import tesserocr
from PIL import Image


for i in range(1,5):
    str = 'code{}.jpg'.format(i)

    image = Image.open(str)

    # image = image.convert('L').show()  直接将图片进行灰度描绘后显示出来.show()
    image = image.convert('L')

    #色彩范围0-256  设置中间值 避免色彩需要过渡
    #超参数
    threshold = 150
    table = []

    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    #将槽点去除了不少
    image = image.point(table,'1')
    image.show()

    result = tesserocr.image_to_text(image)
    print(result)