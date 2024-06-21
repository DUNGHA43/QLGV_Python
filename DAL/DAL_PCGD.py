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