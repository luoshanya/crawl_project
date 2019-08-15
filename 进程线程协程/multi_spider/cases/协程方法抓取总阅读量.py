# 用asyncio和aiohttp抓取博客的总阅读量 (提示:先用接又找到每篇文章的链接)
# https://www.jianshu.com/u/130f76596b02

import re
import asyncio
import aiohttp
import requests
import ssl
from lxml import etree
from asyncio.queues import Queue
from aiosocksy import Socks5Auth
from aiosocksy.connector import ProxyConnector, ProxyClientRequest

class Common():
    task_queue = Queue()
    result_queue = Queue()
    result_queue_1 = []

async def session_get(session,url,socks):
    auth = Socks5Auth(login='...', password='...')
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    timeout = aiohttp.ClientTimeout(total=20)
    response = await session.get(
        url,
        proxy=socks,
        proxy_auth=auth,
        timeout=timeout,
        headers=headers,
        ssl=ssl.SSLContext()
    )
    return await response.text(), response.status

async def download(url):
    connector = ProxyConnector()
    socks = None
    async with aiohttp.ClientSession(
            connector = connector,
            request_class = ProxyClientRequest
    ) as session:
        ret, status = await session_get(session, url, socks)
        if 'window.location.href' in ret and len(ret) < 1000:
            url = ret.split("window.location.href='")[1].split("'")[0]
            ret, status = await session_get(session, url, socks)
        return ret, status

async def parse_html(content):
    read_num_pattern = re.compile(r'"views_count":\d+')
    read_num = int(read_num_pattern.findall(content)[0].split(':')[-1])
    return read_num

def get_all_article_links():
    links_list = []
    for i in range(1,21):
        url = 'https://www.jianshu.com/u/130f76596b02?order_by=shared_at&page={}'.format(i)
        header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        response = requests.get(url,
                                headers=header,
                                timeout=5
                                )
        tree = etree.HTML(response.text)
        article_links = tree.xpath('//div[@class="content"]/a[@class="title"]/@href')
        for item in article_links:
            article_link = 'https://www.jianshu.com' + item
            links_list.append(article_link)
            print(article_link)
    return links_list

async def down_and_parse_task(queue):
    while 1:
        try:
            url = queue.get_nowait()
        except:
            return
        error = None
        for retry_cnt in range(3):
            try:
                html, status = await download(url)
                if status != 200:
                    html, status = await download(url)
                read_num = await parse_html(html)
                print(read_num)
                # await Common.result_queue.put(read_num)
                Common.result_queue_1.append(read_num)
                break
            except Exception as e:
                error = e
                await asyncio.sleep(0.2)
                continue
        else:
            raise error

async def count_sum():
    while 1:
        try:
            print(Common.result_queue_1)
            print('总阅读量 = ',sum(Common.result_queue_1))
            await asyncio.sleep(3)
        except:
            pass

async def main():
    all_links = get_all_article_links()
    for item in set(all_links):
        await Common.task_queue.put(item)
    for _ in range(10):
        loop.create_task(down_and_parse_task(Common.task_queue))
    loop.create_task(count_sum())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()