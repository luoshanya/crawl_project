import json
import csv
import pandas as pd

#1.打开json文件 创建一个CSV文件
#格式不对utf-8,pycharm里面可以看到内容，但是如果在Windows系统上看表格就会乱码，不写结果则反过来
# create_csv = open('json_data/data01.csv','w', encoding='gbk')

# #2.读取文件内容，将内容转换列表
# 转换文章解读的代码
def jiedu_title():
    open_json_data = open('json_data/2019-08-22-10-53-59-文章解读.json','r', encoding="utf-8")
    json_data = json.load(open_json_data)
    values_list = []
    key_list = []
    key_data = ['account', 'detail', 'news_articles']
    for ke in key_data:
        if ke == 'news_articles':
            key_list.append(json_data[0][ke][0].keys())
        else:
            key_list.append(json_data[0][ke].keys())
    keys_list = [a for i in key_list for a in i]
    # print(keys_list)
    for i in json_data:
        data = []
        for ke in key_data:
            if ke == 'news_articles':
                for key in json_data[0][ke][0].keys():
                    try:
                        value = i[ke][0][key]
                        data.append(value)
                    except KeyError:
                        # print(key)
                        data.append('')
                    except TypeError:
                        print(key)
                values_list.append(data)
                # print(len(values_list[0]))
            else:
                for key in json_data[0][ke].keys():
                    if key == 'like_nums':
                        value = i[ke][key]
                        data.append(value)
                    else:
                        try:
                            value = i[ke][key]
                            data.append(value)
                        except KeyError:
                            data.append('')
                        except TypeError:
                            print(key)
        values_list.append(data)
    print(values_list[0])

    csv_data = pd.DataFrame(columns=keys_list, data=values_list)
    print(csv_data)
    csv_data.to_csv("json_data/解3数据.csv", encoding="gb18030")
    open_json_data.close()

# 转换排名上升的方法
def gzh_pm_s():
    open_json_data = open('json_data/2019-08-22-10-53-34-排名上升.json', 'r', encoding="utf-8")
    json_data = json.load(open_json_data)
    keys = json_data[0]['data'][0].keys()
    data = []
    for i in json_data:
        #values(内容) 将i循环的数据放进data里
        values = i['data']
        for a in values:
            list_data = []
            for i in a.values():
                list_data.append(i)
            data.append(list_data)
    print(data)
    csv_data = pd.DataFrame(columns=keys, data=data)
    print(csv_data)
    csv_data.to_csv("json_data/公众号排行趋势数据.csv", encoding="gb18030")
    open_json_data.close()
gzh_pm_s()

#
# print(json_data[0])
# data = []
# # #表头需要指定的内容，不能直接放进；列表
# list_data = []
# j_data = ['account', 'detail', 'news_articles', 'other_articles']
# for i in j_data:
#     if i in ['account', 'detail']:
# list_data.append(json_data_key)
    # else:
# json_data_key = json_data[0][i]
# for i in json_data_key:
#     json_data_keys = i.keys()
#     list_data.append(json_data_keys)

# for value in json_data:
#     vue = value['account']
#     data.append(vue.values())
    # vue = value['account']
    # for vua in vue:
    #     data.append(vua.values())

# print(data)
# print(list_data[0])

# json格式的转化csv
# json_data_values = json_data[0].values()
# data02 = []
# for data01 in json_data_values:
#     json_data_keys = data01.keys()
#     for i in json_data_keys:
#         data02.append(i)
# data = []
# for i in json_data:
#     #values(内容) 将i循环的数据放进data里
#     values = i.values()
#     list_data = []
#     for a in values:
#         for i in a.values():
#             a = list_data.append(i)
#         if list_data not in data:
#             data.append(list_data)
# print(data)

#3.创建CSV写入器
# write = csv.writer(create_csv)

#4.将内容写入csv
#表头是row  内容用writerows
# write.writerow(list_data[0])

# write.writerows(data)
#
# #5.关闭文件
# create_csv.close()
# open_json_data.close()


