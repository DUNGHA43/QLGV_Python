import mysql.connector as db
from . import ConnectDB

def showAccountAll():
    conn = ConnectDB.Connect()
    qr = r"SELECT taiKhoan, matKhau, hoTen FROM tbltaikhoan AS tk INNER JOIN tblgiangvien AS gv ON gv.maGV = tk.maGV;"
    cs = conn.cursor()
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()
    return rs

def addAccount(taiKhoan, matKhau, maGV):
    try:
        conn = ConnectDB.Connect()
        cs = conn.cursor()
        new_TK = (taiKhoan, matKhau, maGV)
        qr = "INSERT INTO tbltaikhoan (taiKhoan, matKhau, quyen, maGV) values ( %s, %s, 2, %s)"
        cs.execute(qr, new_TK)
        conn.commit()
        conn.close()
        return cs.rowcount
    except:
        return 0
def updateAccount(taiKhoan, matKhau, maGV):
    try:
        conn = ConnectDB.Connect()
        cs = conn.cursor()
        new_TK = (matKhau, maGV, taiKhoan)
        qr = "UPDATE tbltaikhoan SET matKhau = %s, maGV = %s WHERE taiKhoan = %s"
        cs.execute(qr, new_TK)
        conn.commit()
        conn.close()
        return cs.rowcount
    except:
        return 0
def deleteAccount(taiKhoan):
    try:
        conn = ConnectDB.Connect()
        cs = conn.cursor()
        qr = "DELETE FROM tbltaikhoan WHERE taiKhoan = %s"
        cs.execute(qr, (taiKhoan,))
        conn.commit()
        conn.close()
        return cs.rowcount
    except:
        return 0

def timKiem(hoTen):
    conn = ConnectDB.Connect()
    qr = r"SELECT taiKhoan, matKhau, hoTen FROM tbltaikhoan AS tk INNER JOIN tblgiangvien AS gv ON gv.maGV = tk.maGV WHERE hoTen LIKE '%"+hoTen+r"%';"
    cs = conn.cursor()
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()
    return rs