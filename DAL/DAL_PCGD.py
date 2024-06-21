import mysql.connector as db
from . import ConnectDB

def showPCGDAll():
    conn = ConnectDB.Connect()
    qr = r"SELECT maPCGD, hoTen, pc.maHocPhan, pc.maPhong, pc.maLop, ngayBatDau, ngayKetThuc, thuHoc, caHoc FROM tblphanconggd as pc inner join tblgiangvien as gv on pc.maGV = gv.maGV order by maPCGD asc;"
    cs = conn.cursor()
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()
    return rs

def showHocPhan():
    conn = ConnectDB.Connect()
    qr = r"select * from tblctdaotao"
    cs = conn.cursor()
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()
    return rs

def showPhongHoc():
    conn = ConnectDB.Connect()
    qr = r"select * from tblphonghoc"
    cs = conn.cursor()
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()
    return rs

def showLop():
    conn = ConnectDB.Connect()
    qr = r"select * from tbllop"
    cs = conn.cursor()
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()
    return rs

def addPCGD(maGV, maHocPhan, maPhong, maLop, ngayBatDau, ngayKetThuc, thuHoc, caHoc):
    try:
        conn = ConnectDB.Connect()
        cs = conn.cursor()
        new_PCGD = ("PCGD"+(str)(ConnectDB.generateNew("tblphanconggd", "maPCGD", "PCGD")), maGV, maHocPhan, maPhong, maLop, ngayBatDau, ngayKetThuc, thuHoc, caHoc)
        qr = "INSERT INTO tblphanconggd (maPCGD, maGV, maHocPhan, maPhong, maLop, ngayBatDau, ngayKetThuc, thuHoc, caHoc) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cs.execute(qr, new_PCGD)
        kt = conn.commit()
        conn.close()
        return cs.rowcount
    except:
         return 0
def updatePCGD(maPCGD, maGV, maHocPhan, maPhong, maLop, ngayBatDau, ngayKetThuc, thuHoc, caHoc):
    try:
        conn = ConnectDB.Connect()
        cs = conn.cursor()
        new_PCGD = (maGV, maHocPhan, maPhong, maLop, ngayBatDau, ngayKetThuc, thuHoc, caHoc, maPCGD)
        qr = "UPDATE tblphanconggd SET maGV = %s, maHocPhan = %s, maPhong = %s, maLop = %s, ngayBatDau = %s, ngayKetThuc = %s, thuHoc = %s, caHoc = %s WHERE maPCGD = %s"
        cs.execute(qr, new_PCGD)
        kt = conn.commit()
        conn.close()
        return cs.rowcount
    except:
        return 0
def deletePCGD(maPCGD):
    try:
        conn = ConnectDB.Connect()
        cs = conn.cursor()
        qr = "DELETE FROM tblphanconggd WHERE maPCGD = %s"
        cs.execute(qr, (maPCGD,))
        kt = conn.commit()
        conn.close()
        return cs.rowcount
    except:
        return 0
def timKiemCGD(maPCGD):
    conn = ConnectDB.Connect()
    qr = r"SELECT maPCGD, hoTen, pc.maHocPhan, pc.maPhong, pc.maLop, ngayBatDau, ngayKetThuc, thuHoc, caHoc FROM tblphanconggd as pc inner join tblgiangvien as gv on pc.maGV = gv.maGV where hoTen like '%"+maPCGD+r"%'  order by maPCGD asc;"
    cs = conn.cursor()
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()
    return rs