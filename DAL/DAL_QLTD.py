import mysql.connector as db
from . import ConnectDB

def showPCGDAll():
    conn = ConnectDB.Connect()
    qr = r"SELECT * FROM tblgiamsatgd order by maGS asc;"
    cs = conn.cursor()
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()
    return rs

def addQLTD(maPCGD, soTietNghi, ngayNghi, soTietBu, ngayBu, ketQua, ghiChu):
    try:
        conn = ConnectDB.Connect()
        cs = conn.cursor()
        new_PCGD = ("GS"+str(ConnectDB.generateNew("tblgiamsatgd", "maGS", "GS")), maPCGD, soTietNghi, ngayNghi, soTietBu, ngayBu, ketQua, ghiChu)
        qr = "INSERT INTO tblgiamsatgd (maGS, maPCGD, soTietNghi, ngayNghi, soTietBu, ngayBu, ketQua, ghiChu) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cs.execute(qr, new_PCGD)
        kt = conn.commit()
        conn.close()
        return cs.rowcount
    except:
         return 0
    
def updateQLTD(maGS, maPCGD, soTietNghi, ngayNghi, soTietBu, ngayBu, ketQua, ghiChu):
    try:
        conn = ConnectDB.Connect()
        cs = conn.cursor()
        new_PCGD = (maPCGD, soTietNghi, ngayNghi, soTietBu, ngayBu, ketQua, ghiChu, maGS)
        qr = "UPDATE tblgiamsatgd SET maPCGD = %s, soTietNghi = %s, ngayNghi = %s, soTietBu = %s, ngayBu = %s, ketQua = %s, ghiChu = %s WHERE maGS = %s"
        cs.execute(qr, new_PCGD)
        kt = conn.commit()
        conn.close()
        return cs.rowcount
    except:
         return 0

def deleteQLTD(maGS):
    try:
        conn = ConnectDB.Connect()
        cs = conn.cursor()
        qr = "DELETE FROM tblgiamsatgd WHERE maGS = %s"
        cs.execute(qr, (maGS,))
        kt = conn.commit()
        conn.close()
        return cs.rowcount
    except:
        return 0
    
def timKiem(maPCGD):
    conn = ConnectDB.Connect()
    qr = r"SELECT * FROM tblgiamsatgd WHERE maPCGD LIKE '%"+maPCGD+r"%';"
    cs = conn.cursor()
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()
    return rs