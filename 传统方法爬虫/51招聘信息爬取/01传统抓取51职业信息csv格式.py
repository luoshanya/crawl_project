import json
import csv

#1.打开json文件 创建一个CSV文件
open_json_data = open('02抓取51职业信息实习版.json','r')
#格式不对utf-8,pycharm里面可以看到内容，但是如果在Windows系统上看表格就会乱码，不写结果则反过来
create_csv = open('02抓取51职业信息实习版.csv','w')


#2.读取文件内容，将内容转换列表
json_data = json.load(open_json_data)
#表头需要指定的内容，不能直接放进；列表
json_data_keys = json_data[0].keys()

data = []
for i in json_data:
    #values(内容) 将i循环的数据放进data里
    data.append(i.values())

#3.创建CSV写入器
write = csv.writer(create_csv)

#4.将内容写入csv
#表头是row  内容用writerows
write.writerow(json_data_keys)

write.writerows(data)

#5.关闭文件
create_csv.close()
open_json_data.close()


