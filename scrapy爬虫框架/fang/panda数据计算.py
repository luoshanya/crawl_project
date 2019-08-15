import pandas as pd

#pandas数据化 下面的命令中json格式只能是一个个字典 然后修改编码格式
df = pd.read_json('old_house.json',lines=True,encoding='utf-8')
# print(df)
#字段个数
# print(df.columns)

#使用pandas的describe()方法 打印相关信息
# print(df.discribe())

#按照区分 分别统计个数
print(
    df['province'].value_counts()
)
