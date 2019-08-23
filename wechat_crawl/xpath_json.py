from jsonpath_rw import parse, jsonpath
import json

file = open('json_data/2019-08-20-jd_data.json', 'r', encoding='utf-8')
data = json.load(fp=file)[0]
jsonpath_rew = parse('$..account')
res = jsonpath_rew.find(data)
j_data = [match.value for match in res][0]
for key,value in j_data.items():
    # for key,value in i.items():
    print(value)
    print(key)
# print(j_data)
file.close()