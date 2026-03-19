import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from cipher.ui.ecc_ui import Ui_MainWindow 

class ECCApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        self.ui.btn_gen_keys.clicked.connect(self.call_api_gen_keys)
        self.ui.btn_sign.clicked.connect(self.call_api_sign)
        self.ui.btn_verify.clicked.connect(self.call_api_verify)

   
    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/ecc/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                QMessageBox.information(self, "Thông báo", response.json()["message"])
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không kết nối được server: {e}")

   
    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/ecc/sign"
       
        payload = {"message": self.ui.txt_info.toPlainText()}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
        
                self.ui.txt_sign.setPlainText(response.json()["signature"])
                QMessageBox.information(self, "Thành công", "Đã tạo chữ ký ECC!")
        except Exception as e:
            print(f"Error: {e}")


    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/ecc/verify"
        payload = {
            "message": self.ui.txt_info.toPlainText(),
            "signature": self.ui.txt_sign.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                result = response.json()["is_verified"]
                if result:
                    QMessageBox.information(self, "Kết quả", "Chữ ký HỢP LỆ (True)")
                else:
                    QMessageBox.warning(self, "Kết quả", "Chữ ký GIẢ MẠO (False)")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ECCApp()
    window.show()
    sys.exit(app.exec_())