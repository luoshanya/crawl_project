# 脚本1

import requests
import json
import redis
import time


class IpProxies:
	def ipGenerator(self):

		r = redis.Redis('127.0.0.1', 6379)
		# add 50/min kuaidaili
		http_ip = 'http://http.tiqu.qingjuhe.cn/getip?num=3&type=2&pro=&city=0&yys=0&port=11&pack=9274&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=0&regions='

		response = requests.get(http_ip)
		# print(response.text)

		ip_json = json.loads(response.text)
		# print(ip_json)
		# {"code":0,"success":true,"msg":"0","data":[{"ip":"180.95.169.87","port":4369,"expire_time":"2018-12-18 22:42:03"},{"ip":"182.127.84.177","port":43621,"expire_time":"2018-12-18 21:04:02"},{"ip":"182.101.230.25","port":43561,"expire_time":"2018-12-18 21:00:03"}]}

		data = ip_json["data"]
		# print(data)

		proxy_list = data
		print(proxy_list)
		
		# # key_list = r.keys('*')

		# proxy_list = ['171.43.18.202:28819,2112', '106.112.172.255:23724,600', '175.151.221.5:28703,991']

		for item in proxy_list:
			print(item)
			# item = item.split(',')
			# ip_port = item[0].split(':')
			# ip = ip_port[0]
			# port = ip_port[1]
			# ip_int = int(ip.replace(".",""))
			ip = item['ip']
			port = item['port']
			
			expire_time = item['expire_time']
			# current_time = int(time.time())
			# expire_time = current_time + int(item[1])
			print(ip, port, expire_time)
			# proxy_item = {"ip":ip, "port":port, "expire_time":expire_time}
			proxy_item = {"schema":"http", "host": ip, "port": port, "expire_time": expire_time, "account": "", "password": "", "count": 2}

			ip_list_formal = []
			proxy_item_all = r.smembers('temp_kuai_formal') #代理池1

			# 对代理池中的代理做去重
			for proxy_temp in proxy_item_all:
				print(proxy_item)
				#eval是将列表、字典等于str转换 相当于把双引号去掉
				item_json = eval(proxy_temp)
				print(item_json)
				ip_formal = item_json["host"]
				port_formal = item_json["port"]
				ip_port_formal = ip_formal + ":" + port_formal
				if ip_port_formal not in ip_list_formal:
					ip_list_formal.append(ip_port_formal)
				else:
					print("duplicating:", proxy_temp)
					r.srem("temp_kuai", proxy_item)
			
			ip_port = ip + ":" + port
			if ip_port not in ip_list_formal:
				print('Add:',json.dumps(proxy_item))
				r.sadd('temp_kuai_formal', json.dumps(proxy_item))


if __name__ == '__main__':
	my_ip = IpProxies()
	my_ip.ipGenerator()