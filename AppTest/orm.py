import sqlite3
import logging

logging.basicConfig(level=logging.INFO)

DB_FILE_PATH = "F:\python\Web01\db.sqlite3"

def drop_table(table):
    """如果表存在,则删除表，如果表中存在数据的时候，使用该
    方法的时候要慎用！"""
    print(DB_FILE_PATH)
    if table is not None and table != "":
        sql = "DROP TABLE IF EXISTS " + table
        logging.info("执行sql:[{}]".format(sql))
        try:
            conn = sqlite3.connect(DB_FILE_PATH)
            cursor = conn.cursor()
            cursor.execute(sql)
            cursor.close()
            conn.commit()
            conn.close()
        except BaseException as e:
            raise


def create_table(sql):
    """创建数据库表：user"""
    logging.info("执行sql:[{}]".format(sql))
    if sql is not None and sql != "":
        try:
            conn = sqlite3.connect(DB_FILE_PATH)
            cursor = conn.cursor()
            cursor.execute(sql)
            cursor.close()
            conn.commit()
            conn.close()
        except BaseException as e:
            raise


def save(sql, data):
    """插入数据"""
    if data is not None:
        try:
            conn = sqlite3.connect(DB_FILE_PATH)
            cursor = conn.cursor()
            for d in data:
                logging.info("执行sql:[{}],参数：[{}]".format(sql, d))
                cursor.execute(sql, d)
            cursor.close()
            conn.commit()
            conn.close()
        except BaseException as e:
            raise


def fetchall(sql):
    """查找所有数据"""
    try:
        conn = sqlite3.connect(DB_FILE_PATH)
        cursor = conn.cursor()
        cursor.execute(sql)
        values = cursor.fetchall()

        for row in values:
            print("ID=%s, name=%s" % (row[0],row[1]))

        if len(values) > 0:
            for row in range(len(values)):
                print(values[row])

        cursor.close()
        conn.commit()
        conn.close()
    except BaseException as e:
        raise

def update(sql, data):
    """更新数据"""
    if data is not None:
        try:
            conn = sqlite3.connect(DB_FILE_PATH)
            cursor = conn.cursor()
            for d in data:
                logging.info("执行sql:[{}],参数：[{}]".format(sql, d))
                cursor.execute(sql, d)
            cursor.close()
            conn.commit()
            conn.close()
        except BaseException as e:
            raise

def detele(sql, data):
    """更新数据"""
    if data is not None:
        try:
            conn = sqlite3.connect(DB_FILE_PATH)
            cursor = conn.cursor()
            for d in data:
                logging.info("执行sql:[{}],参数：[{}]".format(sql, d))
                cursor.execute(sql, d)
            cursor.close()
            conn.commit()
            conn.close()
        except BaseException as e:
            raise

def exeute(sql, args):
    pass

#删除表
drop_table("user")

#创建表
sql = "create  table user  (id varchar(20) primary key, name varchar(20))"
create_table(sql)

#插入数据
sql = r"insert into user values (?, ?)"
data = [(1, 'Hongten'),
        (2, 'Tom'),
        (3, 'Jake'),
        (4, 'Cate')]
save(sql, data)

#查找
sql = "select * from user"
fetchall(sql)

# 更新
update_sql = 'UPDATE student SET name = ? WHERE ID = ? '
data = [('HongtenAA', 1),
        ('HongtenBB', 2),
        ('HongtenCC', 3),
        ('HongtenDD', 4)]
update(update_sql, data)


