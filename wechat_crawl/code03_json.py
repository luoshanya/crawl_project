import json

file = open('data.json', 'r', encoding='utf-8')
datas = json.load(fp=file)
for i in datas:
    data = i['data'][0]['id']
    print(data)
    # for a in data:
    #     print(a['id'])