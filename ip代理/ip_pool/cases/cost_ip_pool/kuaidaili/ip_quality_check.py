# 脚本3

import redis
import time
import telnetlib


r = redis.Redis('127.0.0.1', 6379)


def verify_ip_pool():
    
    proxy_item_all = r.smembers('all_kuai_formal')
    # print(proxy_item_all)
    for proxy_item in proxy_item_all:
        proxy_item_dict = eval(proxy_item)
        print(proxy_item_dict)
        ip = proxy_item_dict["host"]
        # print(ip)

        port = proxy_item_dict["port"]
        # print(port)

        expire_time = proxy_item_dict["expire_time"]
        # print(expire_time)

        current_time = int(time.time())
        if expire_time < current_time:
            print("expired and delete")
            r.srem('all_kuai_formal', proxy_item)
        else:
            print("still available")

            try:
                telnetlib.Telnet(ip, port=port, timeout=1)  # 用telnet对ip进行验证
                print('success', ip, port)
            except:
                print('=== fail and delete ===', ip, port)
                r.srem('all_kuai_formal', proxy_item)



if __name__ == '__main__':
    try:
        print("=================================")
        verify_ip_pool()
    except Exception as e:
        print(e)