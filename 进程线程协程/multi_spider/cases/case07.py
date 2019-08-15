#coding:utf-8

import re
import ssl
import csv
import json
import time
import random
import asyncio
import aiohttp
import requests
from lxml import etree
from asyncio.queues import Queue
from aiosocksy import Socks5Auth
from aiosocksy.connector import ProxyConnector, ProxyClientRequest


class Common():
    #创建队列实例   引进的是asyncio的队列
    task_queue = Queue()
    result_queue = Queue()
    market_cap_all = 0
    currency_rate = 0

# 线上内网
socks5_address_prod = [
    'socks5://10.1.100.253:1235',
    'socks5://10.1.100.51：1235',
    'socks5://10.1.100.70：1235',
    'socks5://10.1.100.205：1235',
    'socks5://10.1.100.73：1235'
]

# 办公网
socks5_address_dev = [
    'socks5://18.208.81.123:1235',
    'socks5://34.197.217.25:1235',
    'socks5://52.20.255.43:1235',
    'socks5://34.237.163.87:1235',
    'socks5://18.208.81.123:1235',
    'socks5://52.0.114.155:1235'
]

DEPLOY_MODE = "dev"

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
    #如果为开发者模式 不使用代理
    if DEPLOY_MODE == "dev":
        socks = None
    #如果为生产者模式就使用代理
    elif DEPLOY_MODE == "Prod":
        socks = random.choice(socks5_address_prod)
    async with aiohttp.ClientSession(
            connector = connector,
            request_class = ProxyClientRequest
    ) as session:
        ret, status = await session_get(session, url, socks)
        if 'window.location.href' in ret and len(ret) < 1000:
            url = ret.split("window.location.href='")[1].split("'")[0]
            ret, status = await session_get(session, url, socks)
        return ret, status

async def parse_html(cid, url, response):
    coin_info = {}
    coin_value = {}

    coin_info['url'] = url
    coin_info['cid'] = cid
    coin_info['time'] = int(time.time())

    tree = etree.HTML(response)

    try:
        price_usd = tree.xpath(
            '//div[@class="priceInfo"]/div[@class="sub"]/span[1]/text()'
        )[0].strip().replace('$', '')
        if '?' not in price_usd:
            coin_value['price'] = float(price_usd)
    except:
        pass

    try:
        updown = tree.xpath(
            '//div[@class="priceInfo"]/div[@class="sub smallfont"]/span[1]/text()'
        )[0].strip().replace('%', '')
        coin_value['updown'] = float(updown)
    except:
        pass

    try:
        volume_24h_rmb = tree.xpath(
            '//div[@class="info"]/div[@class="charCell"][2]/div[2]/span/text()'
        )[0].strip().replace('¥', '').replace(',', '')
        coin_value['volume_24h'] = int(float(volume_24h_rmb) / Common.currency_rate)
    except:
        pass

    try:
        circulating_supply = tree.xpath(
            '//div[@class="info"]//div[@class="charCell"][1]/div[@class="val"]/text()'
        )[0].strip().replace(',', '')
        if '?' not in circulating_supply:
            circulating_supply = re.match(r'^(\d+)(\w+)$', circulating_supply).group(1)
            coin_value['circulating_supply'] = int(circulating_supply)
    except:
        pass

    try:
        if coin_value['price'] and coin_value['circulating_supply']:
            market_cap = coin_value['price'] * coin_value['circulating_supply']
            coin_value['market_cap'] = market_cap
    except:
        pass

    try:
        if coin_value['market_cap']:
            global_share = coin_value['market_cap'] / Common.market_cap_all
            if global_share < 0.001:
                coin_value['global_share'] = '<0.1%'
            else:
                coin_value['global_share'] = str((global_share * 100).__round__(2)) + '%'
    except:
        pass

    try:
        circulation_rate = tree.xpath(
            '//div[@class="info"]//div[@class="charbox"][1]/div[@class="val"]/text()'
        )[0].strip()
        if '?' not in circulation_rate:
            coin_value['circulation_rate'] = circulation_rate
    except:
        pass

    try:
        turnover_rate = tree.xpath(
            '//div[@class="info"]//div[@class="charbox"][1]/div[@class="val"]/text()'
        )[1].strip()
        if '?' not in turnover_rate:
            coin_value['turnover_rate'] = turnover_rate
    except:
        pass

    try:
        issue_time = tree.xpath(
            '//div[@class="infoList"]/div[1]/div[1]/span[2]/text()'
        )[0].strip()
        if issue_time != '－':
            coin_value['issue_time'] = issue_time
    except:
        pass

    try:
        exchange_num = tree.xpath(
            '//div[@class="infoList"]/div[3]/div[1]/span[2]/text()'
        )[0].strip().replace('家', '')
        coin_value['exchange_num'] = int(exchange_num)
    except:
        pass

    try:
        total_circulation = tree.xpath(
            '//div[@class="infoList"]/div[2]/div[2]/span[2]/text()'
        )[0].strip().replace(',', '')
        coin_value['total_circulation'] = int(total_circulation)
    except:
        pass

    coin_info['value'] = coin_value
    return coin_info

async def down_and_parse_task(queue):
    while 1:
        try:
            cid, url = queue.get_nowait()[:2]
        except:
            return
        for retry_cnt in range(3):
            try:
                html, status = await download(url)
                if status != 200:
                    html, status = await download(url)
                if '访问控制拒绝了你的请求' in html:
                    html, status = await download(url)
                html_parse_result = await parse_html(cid, url, html)
                print(html_parse_result)
                await Common.result_queue.put(html_parse_result)
                break
            except:
                await asyncio.sleep(0.2)
                continue

async def push(data):
    url = 'http://127.0.0.1:8000/aaa'
    error = None
    for retry_cnt in range(3):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                        url,
                        data=json.dumps(data)
                ) as response:
                    pass
                response.raise_for_status()
        except Exception as e:
            await asyncio.sleep(0.2)
            print(e)

async def speed_monitor():
    while Common.task_queue.qsize() != 0:
        old_queue_len = Common.task_queue.qsize()
        await asyncio.sleep(5)
        new_queue_count = Common.task_queue.qsize()
        print('=================')
        print('speed = ', (old_queue_len - new_queue_count) / 5)

async def monitor_finish():
    while len(asyncio.Task.all_tasks()) > 3:
        await asyncio.sleep(1)
    await asyncio.sleep(5)
    raise SystemExit()

async def push_results():
    temp_q = []
    while 1:
        try:
            await asyncio.sleep(3)
            for _ in range(Common.result_queue.qsize()):
                temp_q.append(await Common.result_queue.get())
            if len(temp_q) > 0:
                await push(temp_q)
                temp_q.clear()
        except:
            import traceback
            print(traceback.format_exc())

async def get_marketcap():
    #api url
    url = 'https://dncapi.feixiaohao.com/api/home/global?webp=0'
    response = requests.get(url)
    response_json = json.loads(response.text)
    #取到json格式里['data']['marketcapvol']    data里的marketcapvol的参数
    marketcap = response_json['data']['marketcapvol']
    Common.market_cap_all = int(marketcap)

async def get_currency_rate():
    url_rate = 'https://dncapi.feixiaohao.com/api/coin/web-rate/'
    response = requests.get(url_rate)
    currency_rate = json.loads(response.text)[11]['cny']
    Common.currency_rate = currency_rate

# 300秒抓取时间上限
async def time_limit():
    await asyncio.sleep(280)
    raise SystemExit()


async def main():
    # loop = asyncio.get_event_loop()
    #取出csv中的每一行数据
    csv_reader = csv.reader(open('feixiaohao_mapping_data.csv', encoding='utf-8'))
    #遍历
    for row in csv_reader:
        try:
            ##这里可以表示为：是否是列表中的那一列第二个元素是否为https
            if row[1].startswith('https'):
                #下面是将row放Common类创建的task_queue里面   调用的话必须写a32222222222222222222222wait
                await Common.task_queue.put(row)
        except:
            pass
    print(Common.task_queue)
    #调用get_marketcap()函数
    await get_marketcap()
    print('总市值', Common.market_cap_all)

    await get_currency_rate()
    print('汇率', Common.currency_rate)

    for _ in range(10):
        loop.create_task(down_and_parse_task(Common.task_queue))
    loop.create_task(monitor_finish())
    loop.create_task(speed_monitor())
    loop.create_task(push_results())
    loop.create_task(time_limit())


if __name__ == '__main__':
    loop= asyncio.get_event_loop()
    loop.create_task(main())
    #run_forever()表示一直运行
    loop.run_forever()