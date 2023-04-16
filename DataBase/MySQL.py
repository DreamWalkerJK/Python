import mysql.connector

mySqlDb = mysql.connector.connect(
    host="localhost",
    user="python",
    passwd="python",
    auth_plugin="mysql_native_password" # mysql 8.0版本密码插件方式为caching_sha2_password，需指定为早期版本mysql_native_password
)

cursor = mySqlDb.cursor()

# cursor.execute("create database demo"); # 创建数据库

# cursor.execute("show databases;") # 查看数据库

# for d in cursor:
#     print(d)

# cursor.execute("use demo;") # 使用数据库

# mySqlDb.commit()    # 数据表增删改必须使用到该语句