# 多进程，使用Process对象

import time
import requests
from multiprocessing import Process

task_list = [
    'https://www.jianshu.com/p/91b702f4f24a',
    'https://www.jianshu.com/p/8e9e0b1b3a11',
    'https://www.jianshu.com/p/7ef0f606c10b',
    'https://www.jianshu.com/p/b117993f5008',
    'https://www.jianshu.com/p/583d83f1ff81'
]

header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

def download(url):
    response = requests.get(url,
                            headers=header,
                            timeout=30
                            )
    print(response.status_code)


if __name__ == '__main__':
    #遍历进程 结果顺序输出
    for item in task_list:
        p = Process(target=download, args=(item,))
        p.start()
        p.join()