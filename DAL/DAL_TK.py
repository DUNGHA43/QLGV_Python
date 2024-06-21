import mysql.connector as db
from . import ConnectDB
import pandas as pd

def showDSGV():
    conn = ConnectDB.Connect()
    qr = r"SELECT maGV, hoTen, tenKhoa, chuyenMon, chucVu, ngaySinh, gioiTinh, soDT, diaChi FROM tblgiangvien as gv inner join tblkhoa as k on k.maKhoa = gv.maKhoa where maGV like '%GV%'"
    cs = conn.cursor()
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()
    return rs

def showTKBGV(hoTen):
    conn = ConnectDB.Connect()
    qr = r"SELECT maPCGD, hoTen, maHocPhan, maPhong, maLop, ngayBatDau, ngayKetThuc, thuHoc, caHoc FROM tblphanconggd as pcgd inner join tblgiangvien as gv on gv.maGV = pcgd.maGV where hoTen like '%"+hoTen+r"%';"
    cs = conn.cursor()
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()
    return rs

def showDSALLPCGD():
    conn = ConnectDB.Connect()
    qr = r"SELECT maPCGD, hoTen, maHocPhan, maPhong, maLop, ngayBatDau, ngayKetThuc, thuHoc, caHoc FROM tblphanconggd as pcgd inner join tblgiangvien as gv on gv.maGV = pcgd.maGV;"
    cs = conn.cursor()
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()
    return rs

def xuatExcel(abc, tenFile):
    try:
        df = pd.DataFrame(abc)
        df.to_excel(r"C:\Users\dungh\Documents\BTL_Python\\"+tenFile+r".xlsx", index=False)
        return 1
    except:
        return 0
