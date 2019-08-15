# 脚本2

import redis
import time
import telnetlib


r = redis.Redis('127.0.0.1', 6379)


def verify_ip_pool():
    proxy_item_all = r.smembers('temp_kuai_formal')
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
        # timeArray = time.strptime(expire_time, "%Y-%m-%d %H:%M:%S")
        # timestamp = time.mktime(timeArray)
        # expire_time = int(timestamp)
        # print(expire_time)

        current_time = int(time.time())
        if expire_time < current_time:
            print("expired and delete")
            r.srem('temp_kuai_formal', proxy_item)
        else:
            print("still available")

            ip_list_formal = []
            #把代理池的内容拿出来
            proxy_item_all = r.smembers('all_kuai_formal')  # 代理池2

            for item in proxy_item_all:
                # print(item)
                item_json = eval(item)
                # print(item_json)
                ip_formal = item_json["host"]
                port_formal = item_json["port"]
                ip_port_formal = ip_formal + ":" + port_formal
                if ip_port_formal not in ip_list_formal:
                    ip_list_formal.append(ip_port_formal)
            
            try:
                telnetlib.Telnet(ip, port=port, timeout=2)  # 用telnet对ip进行验证
                print('success', ip, port)
                # r.sadd('ip_pool_success', proxy_item)
                ip_port = ip + ":" + port
                if ip_port not in ip_list_formal:
                    print("=== add to all_kuai_formal ===")
                    r.sadd('all_kuai_formal', proxy_item)
                else:
                    print("duplicate")
            except:
                print('fail', ip, port)


if __name__ == '__main__':

    try:
        print("=================================")
        verify_ip_pool()
    except Exception as e:
        print(e)