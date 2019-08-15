#aiohttp 意思异步的输入和输出 i input o output
import aiohttp
#a星开o
import asyncio

import ssl

async def fetch(session, url):
    async with session.get(
            url,
        #ssl必须加 不然会在请求的时候报错：ssl错误
            ssl=ssl.SSLContext()
    ) as response:
        return await response.text()

async def main():
    #这是客户端 Client
    async with aiohttp.ClientSession() as session:
        #使用asyncio必须要用await  意思是必须在fetch函数执行完后 html才去拿它的结果
        html = await fetch(session, 'http://www.baidu.com')
        print(html)

#使用之前必须创建一个事件循环
loop = asyncio.get_event_loop()
#调用的时候用run_until_complete()这个方法 里面装函数main()
loop.run_until_complete(main())