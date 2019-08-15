import tesserocr

for i in range(1,6):
    str = 'code{}.jpg'.format(i)
    #这次使用的是file_to_text()方法
    result = tesserocr.file_to_text(str).strip()
    print(result)