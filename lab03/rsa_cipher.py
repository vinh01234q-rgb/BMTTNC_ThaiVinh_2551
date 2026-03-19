import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
try:
    from ui.rsa import Ui_MainWindow
except ImportError:
    from cipher.ui.rsa import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
       
        self.ui.btn_gen_keys.clicked.connect(self.call_api_gen_keys) 
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)     
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)     
        self.ui.btn_sign.clicked.connect(self.call_api_sign)      
        self.ui.btn_verify.clicked.connect(self.call_api_verify)  

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                QMessageBox.information(self, "Thông báo", data["message"])
            else:
                print("Error while calling API")
        except Exception as e:
            print(f"Error: {e}")

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        # Lấy text từ ô txt_plain
        payload = {
            "message": self.ui.txt_plain.toPlainText(),
            "key_type": "public"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # Hiển thị vào ô txt_cipher
                self.ui.txt_cipher.setPlainText(data["encrypted_message"])
                QMessageBox.information(self, "Thành công", "Đã mã hóa dữ liệu!")
        except Exception as e:
            print(f"Error: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        # Lấy cipher từ ô txt_cipher
        payload = {
            "ciphertext": self.ui.txt_cipher.toPlainText(),
            "key_type": "private"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # Trả kết quả về ô txt_plain
                self.ui.txt_plain.setPlainText(data["decrypted_message"])
                QMessageBox.information(self, "Thành công", "Đã giải mã dữ liệu!")
        except Exception as e:
            print(f"Error: {e}")

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"
        # Trong file rsa.py của bạn, ô Information là txt_plain_3
        payload = {
            "message": self.ui.txt_plain_3.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # Ô Signature là txt_plain_4
                self.ui.txt_plain_4.setPlainText(data["signature"])
                QMessageBox.information(self, "Thành công", "Đã ký số thành công!")
        except Exception as e:
            print(f"Error: {e}")

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"
        payload = {
            "message": self.ui.txt_plain_3.toPlainText(),
            "signature": self.ui.txt_plain_4.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if data["is_verified"]:
                    QMessageBox.information(self, "Xác thực", "Chữ ký HỢP LỆ!")
                else:
                    QMessageBox.warning(self, "Xác thực", "Chữ ký KHÔNG đúng!")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())