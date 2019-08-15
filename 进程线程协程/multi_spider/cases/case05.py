#coding:utf-8

# 通过gather方法

import asyncio

async def a(t):
    print('-->', t)
    #这里表示暂停0.5秒 暂停期间协程让出CPU资源 其他协程继续使用 这就是asyncio
    await asyncio.sleep(0.5)
    print('<--', t)
    return t * 10

def main():
    #range(3) 代表从0开始到2 三个数
    futs = [a(t) for t in range(6)]
    print(futs)
    #列表并行执行
    ret = asyncio.gather(*futs)
    print(ret)
    # 创建事件循环 格式固定 loop = asyncio.get_event_loop()  ret = loop.run_until_complete
    loop = asyncio.get_event_loop()

    ret1 = loop.run_until_complete(ret)

    print(ret1)

main()