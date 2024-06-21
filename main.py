import ip
#Cua so dang nhap
class Login_window(ip.QMainWindow):
    def __init__(self):
        super(Login_window, self).__init__()
        ip.uic.loadUi('login.ui', self) 
        #Giao dien login
        self.btnDangNhap.clicked.connect(self.loginApp)
        
    def loginApp(self):
        tk = self.txtTaiKhoan.text()
        mk = self.txtMatKhau.text()
        kt = ip.ConnectDB.loginApp(tk, mk)
        if kt:
            widget.setFixedHeight(541)
            widget.setFixedWidth(899)
            widget.move(250, 100)
            widget.setCurrentIndex(1)
        else:
            ip.QMessageBox.information(self, "Thông báo", "Sai tài khoản hoặc mật khẩu!")
#Cua so giao dien chinh
class MainGui_Window(ip.QMainWindow):
    
    def __init__(self):
        super(MainGui_Window, self).__init__()
        ip.uic.loadUi('mainGui.ui', self)

    # Chuyen giao dien
        self.btnTaiKhoan.clicked.connect(self.switch_to_TaiKhoanGui)
        self.btnGiangVien.clicked.connect(self.switch_to_GiangVienGui)
        self.btnPCGD.clicked.connect(self.switch_to_PCGDGui)
        self.btnQLTD.clicked.connect(self.switch_to_QLTDGui)    
        self.btnThongKe.clicked.connect(self.switch_to_ThongKeGui)
        self.btnDangXuat.clicked.connect(self.click_DangXuat)
    #-----------------------------------------------------------------------
    # Giao dien Quan ly giang vien
        self.showDSGV()
        self.tbDSGV.cellClicked.connect(self.tableDSGV_Clicked)
        self.showKhoa_Combobox()
        self.btnThemGV.clicked.connect(self.themGV)
        self.btnSuaGV.clicked.connect(self.updateGV)
        self.btnXoaGV.clicked.connect(self.xoaGV)
        self.btnTimKiemGV.clicked.connect(self.showDSGV_TimKiem)
    #------------------------------------------------------------------------
    # Giao dien Quan ly tai khoan
        self.showDSTK()
        self.tbDSTaiKhoan.cellClicked.connect(self.tableDSTK_Clicked)
        self.showDSGV_TK_Combobox()
        self.txtTenGV_TK.currentTextChanged.connect(self.selectCB_TenGV_TK)
        self.btnThemTK.clicked.connect(self.themTK)
        self.btnSuaTK.clicked.connect(self.capNhatTK)
        self.btnXoaTK.clicked.connect(self.xoaTK)
        self.btnTimKiemTK.clicked.connect(self.timKiem_TK)
    #------------------------------------------------------------------------
    # Giao dien Phan cong giang day
        self.showDSPCGDALL()
    #------------------------------------------------------------------------
    # Chuyen giao dien
    def switch_to_TaiKhoanGui(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_GiangVienGui(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def switch_to_PCGDGui(self):
        self.stackedWidget.setCurrentIndex(2)
    
    def switch_to_QLTDGui(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_ThongKeGui(self):
        self.stackedWidget.setCurrentIndex(4)

    def click_DangXuat(self):
        self.close()
    #------------------------------------------
    #Giao dien Quan ly giang vien
    def showDSGV(self):
        self.tbDSGV.setRowCount(ip.DAL_GV.showGVAll().__len__())
        self.tbDSGV.setColumnCount(9)
        self.tbDSGV.setHorizontalHeaderLabels(["Mã giảng viên", "Họ tên", "Khoa", "Chuyên môn", "Chức vụ", "Ngày sinh", "Giới tính", "Số điện thoại", "Địa chỉ"])
        self.tbDSGV.setColumnWidth(1, 150)
        self.tbDSGV.setColumnWidth(8, 500)
        table_row = 0
        for row in ip.DAL_GV.showGVAll():
            self.tbDSGV.setItem(table_row, 0, ip.QTableWidgetItem(row[0]))
            self.tbDSGV.setItem(table_row, 1, ip.QTableWidgetItem(row[1]))
            self.tbDSGV.setItem(table_row, 2, ip.QTableWidgetItem(row[2]))
            self.tbDSGV.setItem(table_row, 3, ip.QTableWidgetItem(row[3]))
            self.tbDSGV.setItem(table_row, 4, ip.QTableWidgetItem(row[4]))
            self.tbDSGV.setItem(table_row, 5, ip.QTableWidgetItem((str)(row[5])))
            self.tbDSGV.setItem(table_row, 6, ip.QTableWidgetItem(row[6]))
            self.tbDSGV.setItem(table_row, 7, ip.QTableWidgetItem(row[7]))
            self.tbDSGV.setItem(table_row, 8, ip.QTableWidgetItem(row[8]))
            table_row += 1

    def tableDSGV_Clicked(self, row, column):
        self.txtMaGV.setText(self.tbDSGV.item(row, 0).text())
        self.txtHoTenGV.setText(self.tbDSGV.item(row, 1).text())
        self.txtKhoaGV.setCurrentText(self.tbDSGV.item(row, 2).text())
        self.txtChuyenMonGV.setCurrentText(self.tbDSGV.item(row, 3).text())
        self.txtChucVuGV.setCurrentText(self.tbDSGV.item(row, 4).text())
        date = ip.QDate.fromString(self.tbDSGV.item(row, 5).text(), "yyyy-MM-dd")
        self.txtNgaySinhGV.setDate(date)
        self.txtGioiTinhGV.setCurrentText(self.tbDSGV.item(row, 6).text())
        self.txtSDTGV.setText(self.tbDSGV.item(row, 7).text())
        self.txtDiaChiGV.setPlainText(self.tbDSGV.item(row, 8).text())
        
    def showKhoa_Combobox(self):
        for row in ip.DAL_GV.showGVAll():
            self.txtKhoaGV.addItem(row[2])

    def themGV(self):
        hoTen = self.txtHoTenGV.text()
        khoa = self.txtKhoaGV.currentText()
        chuyenMon = self.txtChuyenMonGV.currentText()
        chucVu = self.txtChucVuGV.currentText()
        ngaySinh = self.txtNgaySinhGV.date().toString("yyyy-MM-dd")
        gioiTinh = self.txtGioiTinhGV.currentText()
        sdt = self.txtSDTGV.text()
        diaChi = self.txtDiaChiGV.toPlainText()
        kt = ip.DAL_GV.addGV(hoTen, khoa, chuyenMon, chucVu, ngaySinh, gioiTinh, sdt, diaChi)
        if kt == 1:
            ip.QMessageBox.information(self, "Thông báo", "Thêm thành công!")
            self.showDSGV()
        else:
            ip.QMessageBox.information(self, "Thông báo", "Thêm không thành công!")

    def updateGV(self):
        maGV = self.txtMaGV.text()
        hoTen = self.txtHoTenGV.text()
        khoa = self.txtKhoaGV.currentText()
        chuyenMon = self.txtChuyenMonGV.currentText()
        chucVu = self.txtChucVuGV.currentText()
        ngaySinh = self.txtNgaySinhGV.date().toString("yyyy-MM-dd")
        gioiTinh = self.txtGioiTinhGV.currentText()
        sdt = self.txtSDTGV.text()
        diaChi = self.txtDiaChiGV.toPlainText()
        kt = ip.DAL_GV.updateGV(maGV, hoTen, khoa, chuyenMon, chucVu, ngaySinh, gioiTinh, sdt, diaChi)
        if kt == 1:
            ip.QMessageBox.information(self, "Thông báo", "Cập nhật thành công!")
            self.showDSGV()
        else:
            ip.QMessageBox.information(self, "Thông báo", "Cập nhật không thành công!")
    def xoaGV(self):
        maGV = self.txtMaGV.text()
        kt = ip.DAL_GV.deleteGV(maGV)
        if kt == 1:
            ip.QMessageBox.information(self, "Thông báo", "Xóa thành công!")
            self.showDSGV()
        else:
            ip.QMessageBox.information(self, "Thông báo", "Xóa không thành công!")
    def showDSGV_TimKiem(self):
        hoTen = self.txtTimKiemGV.text()
        self.tbDSGV.setRowCount(ip.DAL_GV.timKiem(hoTen).__len__())
        self.tbDSGV.setColumnCount(9)
        self.tbDSGV.setHorizontalHeaderLabels(["Mã giảng viên", "Họ tên", "Khoa", "Chuyên môn", "Chức vụ", "Ngày sinh", "Giới tính", "Số điện thoại", "Địa chỉ"])
        self.tbDSGV.setColumnWidth(1, 150)
        self.tbDSGV.setColumnWidth(8, 500)
        table_row = 0
        for row in ip.DAL_GV.timKiem(hoTen):
            self.tbDSGV.setItem(table_row, 0, ip.QTableWidgetItem(row[0]))
            self.tbDSGV.setItem(table_row, 1, ip.QTableWidgetItem(row[1]))
            self.tbDSGV.setItem(table_row, 2, ip.QTableWidgetItem(row[2]))
            self.tbDSGV.setItem(table_row, 3, ip.QTableWidgetItem(row[3]))
            self.tbDSGV.setItem(table_row, 4, ip.QTableWidgetItem(row[4]))
            self.tbDSGV.setItem(table_row, 5, ip.QTableWidgetItem((str)(row[5])))
            self.tbDSGV.setItem(table_row, 6, ip.QTableWidgetItem(row[6]))
            self.tbDSGV.setItem(table_row, 7, ip.QTableWidgetItem(row[7]))
            self.tbDSGV.setItem(table_row, 8, ip.QTableWidgetItem(row[8]))
            table_row += 1
    #----------------------------------------------------------
    # Giao dien Quan ly tai khoan
    def showDSTK(self):
        self.tbDSTaiKhoan.setRowCount(ip.DAL_TaiKhoan.showAccountAll().__len__())
        self.tbDSTaiKhoan.setColumnCount(3)
        self.tbDSTaiKhoan.setHorizontalHeaderLabels(["Tài khoản", "Mật khẩu", "Giảng viên"])
        self.tbDSTaiKhoan.setColumnWidth(2, 180)
        tableRow = 0
        for row in ip.DAL_TaiKhoan.showAccountAll():
            self.tbDSTaiKhoan.setItem(tableRow, 0, ip.QTableWidgetItem(row[0]))
            self.tbDSTaiKhoan.setItem(tableRow, 1, ip.QTableWidgetItem(row[1]))
            self.tbDSTaiKhoan.setItem(tableRow, 2, ip.QTableWidgetItem(row[2]))
            tableRow += 1
    def tableDSTK_Clicked(self, row, column):
        self.txtTaiKhoan.setText(self.tbDSTaiKhoan.item(row, 0).text())
        self.txtMatKhau.setText(self.tbDSTaiKhoan.item(row, 1).text())
        self.txtTenGV_TK.setCurrentText(self.tbDSTaiKhoan.item(row, 2).text())
    def showDSGV_TK_Combobox(self):
        for row in ip.DAL_GV.showGVAll():
            self.txtTenGV_TK.addItem(row[1])
    def selectCB_TenGV_TK(self, text):
        maGV = ip.DAL_GV.timKiem(text)
        self.txtMaGV_TK.setText(str(maGV[0][0]))
    def themTK(self):
        tenTK = self.txtTaiKhoan.text()
        matKhau = self.txtMatKhau.text()
        maGV = self.txtMaGV_TK.text()
        kt = ip.DAL_TaiKhoan.addAccount(tenTK, matKhau, maGV)
        if kt == 1:
            ip.QMessageBox.information(self, "Thông báo", "Thêm tài khoản thành công!")
            self.showDSTK()
        else:
            ip.QMessageBox.information(self, "Thông báo", "Thêm tài không khoản thành công!")
    def capNhatTK(self):
        tenTK = self.txtTaiKhoan.text()
        matKhau = self.txtMatKhau.text()
        maGV = self.txtMaGV_TK.text()
        kt = ip.DAL_TaiKhoan.updateAccount(tenTK, matKhau, maGV)
        if kt == 1:
            ip.QMessageBox.information(self, "Thông báo", "Cập nhật tài khoản thành công!")
            self.showDSTK()
        else:
            ip.QMessageBox.information(self, "Thông báo", "Cập nhật tài không khoản thành công!")
    def xoaTK(self):
        tenTK = self.txtTaiKhoan.text()
        kt = ip.DAL_TaiKhoan.deleteAccount(tenTK)
        if kt == 1:
            ip.QMessageBox.information(self, "Thông báo", "Xóa tài khoản thành công!")
            self.showDSTK()
        else:
            ip.QMessageBox.information(self, "Thông báo", "Xóa tài không khoản thành công!")
    def timKiem_TK(self):
        hoTen = self.txtTimKiemTK.text()
        self.tbDSTaiKhoan.setRowCount(ip.DAL_TaiKhoan.timKiem(hoTen).__len__())
        self.tbDSTaiKhoan.setColumnCount(3)
        self.tbDSTaiKhoan.setHorizontalHeaderLabels(["Tài khoản", "Mật khẩu", "Giảng viên"])
        self.tbDSTaiKhoan.setColumnWidth(2, 180)
        tableRow = 0
        for row in ip.DAL_TaiKhoan.timKiem(hoTen):
            self.tbDSTaiKhoan.setItem(tableRow, 0, ip.QTableWidgetItem(row[0]))
            self.tbDSTaiKhoan.setItem(tableRow, 1, ip.QTableWidgetItem(row[1]))
            self.tbDSTaiKhoan.setItem(tableRow, 2, ip.QTableWidgetItem(row[2]))
            tableRow += 1
    #------------------------------------------------------------------------
    
    # Giao dien Phan cong giang day
    def showDSPCGDALL(self):
        self.tbDSPCGD.setRowCount(ip.DAL_PCGD.showPCGDAll().__len__())
        self.tbDSPCGD.setColumnCount(9)
        self.tbDSPCGD.setHorizontalHeaderLabels(["Mã PCGD", "Giảng viên", "Học phần", "Phòng", "Lớp", "Ngày bắt đầu", "Ngày kết thúc", "Thứ học", "Ca học"])
        self.tbDSPCGD.setColumnWidth(1, 150)
        tableRow = 0
        for row in ip.DAL_PCGD.showPCGDAll():
            self.tbDSPCGD.setItem(tableRow, 0, ip.QTableWidgetItem(row[0]))
            self.tbDSPCGD.setItem(tableRow, 1, ip.QTableWidgetItem(row[1]))
            self.tbDSPCGD.setItem(tableRow, 2, ip.QTableWidgetItem(row[2]))
            self.tbDSPCGD.setItem(tableRow, 3, ip.QTableWidgetItem(row[3]))
            self.tbDSPCGD.setItem(tableRow, 4, ip.QTableWidgetItem(row[4]))
            self.tbDSPCGD.setItem(tableRow, 5, ip.QTableWidgetItem(str(row[5])))
            self.tbDSPCGD.setItem(tableRow, 6, ip.QTableWidgetItem((str)(row[6])))
            self.tbDSPCGD.setItem(tableRow, 7, ip.QTableWidgetItem(row[7]))
            self.tbDSPCGD.setItem(tableRow, 8, ip.QTableWidgetItem(row[8]))
            tableRow += 1
    #------------------------------------------------------------------------

# Main
app = ip.QApplication(ip.sys.argv)
widget = ip.QtWidgets.QStackedWidget()
login_f = Login_window()
mainGui_f = MainGui_Window()
widget.addWidget(login_f)
widget.addWidget(mainGui_f)
widget.setCurrentIndex(0)
widget.setFixedHeight(245)
widget.setFixedWidth(373)
widget.show()
app.exec()