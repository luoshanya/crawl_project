import pymongo

try:
    #1.链接MongoDB数据库
    mongo_python = pymongo.MongoClient()

    #2.创建数据库
    db = mongo_python['six']

    #3.创建表
    collection = db['stu']
        #根据js格式 一起写也行
    # collection = mongo_python['six']['stu']
    #4.写数据
    #单个数据
    one_data = {"name" : '张三',"age" : 18}

    #多个数据
    two_many = [
        {"name": "小米", "age": 18, "gender": 'true'},
        {"name": "小黑", "age": 20, "gender": 'true'},
        {"name": "小明", "age": 18, "gender": 'true'},
        {"name": "小红", "age": 90, "gender": 'false'},
        {"name": "小梦", "age": 78, "gender": 'false'},
        {"name": "小蓝", "age": 38, "gender": 'false'}
    ]

    #5.插入数据
    #插入一条数据：insert_one()
    # collection.insert_one(one_data)

    #插入多条数据 insert_many()
    # collection.insert_many(two_many)
    #查看异常

    #删除一个delete-one    多个就是delete_many
    # collection.delete_one({'age':90})


    #修改数据
    # collection.update_one({"age":20},{"$set":{"name":"小红"}})

    #查找数据   find_one一个数据
    result = collection.find({"age":18})
    # print(result)    显示表示多个 所以要使用遍历才能看到数据<pymongo.cursor.Cursor object at 0x02B92C30>
    for i in result:
        print(i)
except Exception as e:
    print(e)

    #直到最后关闭数据库
finally:
    mongo_python.close()