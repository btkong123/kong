import uuid
import pymysql
import re

def create_code(num, length):
    result = []
    while True:
        uuid_id = uuid.uuid4()
        temp = str(uuid_id).replace('-', '')[:length]
        if not temp in result:
            result.append(temp)
        if len(result) == num:
            break
    return result

def save_to_mysql(num_list):
    conn = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    charset='utf8')
    cursor = conn.cursor()

    sql_create_db = 'CREATE DATABASE IF NOT EXISTS yixiaohan_db'
    cursor.execute(sql_create_db)

    conn.select_db('yixiaohan_db')
    sql_create_table = 'CREATE TABLE IF NOT EXISTS codes(code char(32))'
    cursor.execute(sql_create_table)

    cursor.executemany('INSERT INTO codes values(%s)', num_list)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    codes = create_code(100, 18)
    save_to_mysql(codes)
