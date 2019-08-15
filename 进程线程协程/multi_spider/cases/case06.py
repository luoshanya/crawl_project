#coding:utf-8

import asyncio

# 通过create_task()方法

async def a(t):
    print('-->', t)
    await asyncio.sleep(0.5)
    print('<--', t)
    return t * 10

#使用async创建方法 返回的是协程对象
async def b():
    # loop = asyncio.get_event_loop()

    cnt = 0
    while 1:
        cnt += 1
        #创建协程 cor
        cor = a(cnt)   # coroutine
        # 创建任务 create_task
        resp = loop.create_task(cor)
        await asyncio.sleep(0.1)
        # print(resp)
        #结果是因为执行函数a(cnt) 又因为函数中需要等待0.5秒 又因下面await需要等待0.1秒 所以循环了五次 阻塞还没通 所以一直将1至5阻塞 等到结果前是一到五
        #但又因为阻塞时间到了 上面塞着的1可以出去了 但是a函数还依然存在阻塞 所以只能一个个的输出 就有了后面输出一个6后还有一个1的结果
loop = asyncio.get_event_loop()

loop.run_until_complete(b())