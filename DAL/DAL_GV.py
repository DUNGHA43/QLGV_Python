import mysql.connector as db
from . import ConnectDB

def showGVAll():
    conn = ConnectDB.Connect()
    qr = r"SELECT * FROM ql_giangvien.tblgiangvien WHERE maGV LIKE '%GV%';"
    cs = conn.cursor()
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()
    return rs

def addGV(hoTen, khoa, chuyenMon, chucVu, ngaySinh, gioiTinh, soDT, diaChi):
    try:
        conn = ConnectDB.Connect()
        cs = conn.cursor()
        new_GV = ("GV"+(str)(ConnectDB.generateNew("tblgiangvien", "maGV", "GV")), hoTen, khoa, chuyenMon, chucVu, ngaySinh, gioiTinh, soDT, diaChi)
        qr = "INSERT INTO tblgiangvien (maGV, hoTen, maKhoa, chuyenMon, chucVu, ngaySinh, gioiTinh, soDT, diaChi) values ( %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cs.execute(qr, new_GV)
        kt = conn.commit()
        conn.close()
        return cs.rowcount
    except:
        return 0
def updateGV(maGV, hoTen, khoa, chuyenMon, chucVu, ngaySinh, gioiTinh, soDT, diaChi):
    try:
        conn = ConnectDB.Connect()
        cs = conn.cursor()
        new_GV = (hoTen, khoa, chuyenMon, chucVu, ngaySinh, gioiTinh, soDT, diaChi, maGV)
        qr = "UPDATE tblgiangvien SET hoTen = %s, maKhoa = %s, chuyenMon = %s, chucVu = %s, ngaySinh = %s, gioiTinh = %s, soDT = %s, diaChi = %s WHERE maGV = %s"
        cs.execute(qr, new_GV)
        kt = conn.commit()
        conn.close()
        return cs.rowcount
    except:
        return 0
def deleteGV(maGV):
    try:
        conn = ConnectDB.Connect()
        cs = conn.cursor()
        qr = "DELETE FROM tblgiangvien WHERE maGV = %s"
        cs.execute(qr, (maGV,))
        kt = conn.commit()
        conn.close()
        return cs.rowcount
    except:
        return 0
def timKiem(hoTen):
    conn = ConnectDB.Connect()
    qr = r"SELECT * FROM ql_giangvien.tblgiangvien WHERE maGV LIKE '%GV%' AND hoTen LIKE '%"+hoTen+r"%';"
    cs = conn.cursor()
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()
    return rs