import pymysql


try:
    #1.链接 数据库  链接对象 connection()
    # conn = pymysql.Connect(
    #     # host="localhost",
    #     host="127.0.0.1",
    #     port=3306,
    #     db="area",
    #     user="root",
    #     password="10130503",
    #     charset="utf8"
    # )

    #第二种写法
    dbparams = {
        'host' : "127.0.0.1",
        'port' : 3306,
        'db' : "area",
        'user' : "root",
        'password' : "10130503",
        'charset' : "utf8"
    }
    conn = pymysql.Connect(**dbparams)

    #创建 游标对象 cursor()   类似开启事务

    cur = conn.cursor()
    #2.建库建表；插入数据    execute()是执行的意思

    # for i in range(10,10000):
    #     insert_data = "insert into areas values ({},'人工智能',1)".format(i)
    #     i+= 1
    #     result = cur.execute(insert_data)

    #更新数据
    # update_data = 'update subjects set title="自然科学" where id=4 '
    # result = cur.execute(update_data)

    #查询数据  fetchone查询一条  fetchall 查询所有

    # select_data = 'select * from studentInfo'
    # cur.execute(select_data)
    # # result = cur.fetchall()
    # result = cur.fetchone()
    # print(result)
    #提交事务
    conn.commit()

    #关闭游标
    cur.close()

    #关闭链接
    conn.close()
except Exception as e:
    print(e)
