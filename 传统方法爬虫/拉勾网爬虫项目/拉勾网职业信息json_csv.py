import csv
import json

json_file = open('拉勾网python职业信息.json','r')
csv_create = open('拉勾网职业信息.csv','w')

json_data = json.load(json_file)
print(json_data)
keys_data = json_data[0].keys()
print(keys_data)
list_data = []
for i in json_data:
    list_data.append(i.values())

print(list_data)

#编写csv写入器
# write = csv.writer(csv_create)
# write.writerow(keys_data)
# write.writerows(list_data)
