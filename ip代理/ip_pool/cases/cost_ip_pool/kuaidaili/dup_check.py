import requests
import json
import redis
import time
import urllib.request
import telnetlib

r = redis.Redis('172.17.180.217', 6379) #docker07
# r = redis.Redis('127.0.0.1', 6379)



def dup_check():
    ip_list = []
    proxy_item_all = r.smembers('all_kuai')
    for item in proxy_item_all:
        item_json = eval(item)
        print(item_json)
        ip = item_json["ip"]
        port = item_json["port"]
        ip_port = ip + ":" + port
        if ip_port not in ip_list:
            ip_list.append(ip_port)
        else:
            print("===============")
            print("duplicating : ", ip_port)
            r.srem("all_kuai",item)

    # # print(proxy_item_all)
    # for proxy_item in proxy_item_all:
    #     proxy_item_dict = eval(proxy_item)
    #     print(proxy_item_dict)
    #     ip = proxy_item_dict["ip"]
    #     # print(ip)

    #     port = proxy_item_dict["port"]
    #     # print(port)

    #     expire_time = proxy_item_dict["expire_time"]
    #     # print(expire_time)
    #     # timeArray = time.strptime(expire_time, "%Y-%m-%d %H:%M:%S")
    #     # timestamp = time.mktime(timeArray)
    #     # expire_time = int(timestamp)
    #     # print(expire_time)

    #     current_time = int(time.time())
    #     if expire_time < current_time:
    #         print("expired")
    #         # r.srem('temp_kuai', proxy_item)
    #     else:
    #         print("still available")

    #         ip_list_formal = []
    #         proxy_item_all = r.smembers('all_kuai')

    #         for item in proxy_item_all:
    #             # print(item)
    #             item_json = eval(item)
    #             print(item_json)
    #             ip_formal = item_json["ip"]
    #             port_formal = item_json["port"]
    #             ip_port_formal = ip_formal + ":" + port_formal
    #             if ip_port_formal not in ip_list_formal:
    #                 ip_list_formal.append(ip_port_formal)
            
    #         try:
    #             telnetlib.Telnet(ip, port=port, timeout=2)  # 用telnet对ip进行验证
    #             print('success', ip, port)
    #             # r.sadd('ip_pool_success', proxy_item)
    #             ip_port = ip + ":" + port
    #             if ip_port not in ip_list_formal:
    #                 r.sadd('all_kuai', proxy_item)
    #         except:
    #             print('fail', ip, port)
    
    
    #test
    # proxy_item_all_test = r.smembers('ip_pool_kuai_test')
    # for proxy_item_test in proxy_item_all_test:
    #     proxy_item_dict_test = eval(proxy_item_test)
    #     print(proxy_item_dict_test)
    #     ip_test = proxy_item_dict_test["ip"]
    #     # print(ip)
    #
    #     port_test = proxy_item_dict_test["port"]
    #     # print(port)
    #
    #     expire_time_test = proxy_item_dict_test["expire_time"]
    #     # print(expire_time)
    #
    #     current_time_test = int(time.time())
    #     if expire_time_test < current_time_test:
    #         print("expired and delete")
    #         r.srem('ip_pool_kuai_test', proxy_item_test)
    #     else:
    #         print("still available")
    #
    #         ip_list = []
    #         proxy_item_all_success = r.smembers('ip_pool_success_test')
    #
    #         for item_success in proxy_item_all_success:
    #             # print(item)
    #             item_success_json = eval(item_success)
    #             print(item_success_json)
    #             ip_success = item_success_json["ip"]
    #             port_success = item_success_json["port"]
    #             ip_port_success = ip_success + ":" + port_success
    #             if ip_port_success not in ip_list:
    #                 ip_list.append(ip_port_success)
    #
    #         try:
    #             telnetlib.Telnet(ip_test, port=port_test, timeout=2)  # 用telnet对ip进行验证
    #             print('success', ip_test, port_test)
    #             ip_port_test = ip_test + ":" + port_test
    #             if ip_port_test not in ip_list:
    #                 r.sadd('ip_pool_success_test', proxy_item_test)
    #         except:
    #             print('fail', ip_test, port_test)


# def is_true():
#     return True


if __name__ == '__main__':
    # while is_true():
    try:
        print("=================================")
        dup_check()
        # time.sleep(60)
    except Exception as e:
        print(e)