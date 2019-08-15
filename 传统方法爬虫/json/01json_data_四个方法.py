import json

#严格按照json格式才可以，不然会出错 字符串单包双!!!!!
data = '[{"name":"张三"},{"gae":18},{"name":"李四"},{"gae":18}]'

#1.用str--list json.loads()转换

data_list = json.loads(data)
# print(type(data_list))
# print(data_list)
# <class 'list'>
# [{"name":"张三"},{"gae":18},{"name":"李四"},{"gae":18}]

#2.#list dict转str  json.dumps()
data2 = [{"name":"张三"},{"gae":18},{"name":"李四"},{"gae":18}]
data_str = json.dumps(data2,ensure_ascii=False)
# print(data_str)
# print(type(data_str))


#3.文件对象 和 dict list转换
#旧的用法：
#       data2 = [{"name":"张三"},{"gae":18},{"name":"李四"},{"gae":18}]
#       data_str = json.dumps(data2)
#       with open("01json.json",'w') as f:
#           f.write(data_str)

#存list数据进文件夹时用json.dumps()转换   fp代表file path 即文件路径  dict list 写入文件
# 第一种方法
# fp = open("03json.json",'w')
# data_save = json.dump(data2,fp)
#第二种方法
data_save = json.dump(data2,open("02json.json",'w'))

#读取文件  json.load()

dat_read = json.load(open('02json.json','r'))
#需要打印出来才能看到结果
# print(dat_read)


data3 = {
    "name":"张三",
    "gae" : 18,
    "sex": "男",
    "asd": 20
}

json_str = json.dumps(data3)
print(type(json_str))
print(json_str)
#json.loads()只能转换str类型  json.dumps()能转换dict和list
json_list = json.loads(json_str)
print(json_list)

