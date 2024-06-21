import mysql.connector as db

def Connect():
    conn = db.connect(user='root', password='DUng0403@', host='localhost', database='ql_giangvien')
    return conn

def loginApp(tk, mk):
    db = Connect()
    query = db.cursor()
    query.execute(f"select * from tbltaikhoan where taiKhoan = '{tk}' and matKhau = '{mk}'")
    kt = query.fetchone()
    db.close()
    return kt

def showGVAll(table, ma, key):
    conn = Connect()
    qr = f"SELECT {ma} FROM `{table}` WHERE {ma} LIKE '%{key}%' ORDER BY {ma} ASC;"
    cs = conn.cursor()
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()
    return rs

def generateNew(table, ma, key):
    add = showGVAll(table, ma, key) 
    # Sử dụng partition để lấy phần số
    result = [item[0].partition(key)[2] for item in add]
    index = 1
    for i in result:
        if(index != (int)(i)):
             return index
        index += 1 
    return index
    
