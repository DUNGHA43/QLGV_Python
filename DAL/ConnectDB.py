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

def showGVAll(table):
    conn = Connect()
    qr = f"SELECT maGV FROM `{table}` WHERE maGV LIKE '%GV%' ORDER BY maGV ASC;"
    cs = conn.cursor()
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()
    return rs

def generateNew(table):
    add = showGVAll(table) 
    # Sử dụng partition để lấy phần số
    result = [item[0].partition('GV')[2] for item in add]
    index = 1
    for i in result:
        if(index != (int)(i)):
            return index
        index += 1 
    return index
