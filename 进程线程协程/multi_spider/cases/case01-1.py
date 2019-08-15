# 多进程，使用Pool

import time
import requests
from multiprocessing import Pool

task_list = [
    'https://www.jianshu.com/p/91b702f4f24a',
    'https://www.jianshu.com/p/8e9e0b1b3a11',
    'https://www.jianshu.com/p/7ef0f606c10b',
    'https://www.jianshu.com/p/b117993f5008',
    'https://www.jianshu.com/p/583d83f1ff81',
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
    #状态码status
    return response.status_code


if __name__ == '__main__':
    #代表十个进程  进程越大时间越短
    p = Pool(10)
    #插入时间 time.time.()
    time_old = time.time()
    #遍历列表map
    for item in p.map(download, task_list):
        print(item)
    time_new = time.time()
    #所需时间
    time_cost = time_new - time_old
    print(time_cost)