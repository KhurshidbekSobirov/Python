from os import read
import sys, threading
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit


class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.btn_minus = QPushButton("-")
        self.btn_plus = QPushButton("+")

        self.narx = QLineEdit()
        self.massa = QLineEdit()

        self.edit_text = QLineEdit()
        self.messages = QListWidget()

        self.h_box.addWidget(self.edit_text)
        self.h_box.addWidget(self.massa)
        self.h_box.addWidget(self.narx)
        self.h_box.addWidget(self.btn_plus)
        self.h_box.addWidget(self.btn_minus)






        self.v_box.addWidget(self.messages)
        self.v_box.addLayout(self.h_box)

        self.edit_text.setPlaceholderText("Enter message here...")
        self.narx.setPlaceholderText("Narx...")
        self.massa.setPlaceholderText("Massa...")

        
        self.btn_minus.clicked.connect(self.send_message)
       

        self.btn_plus.clicked.connect(self.send_messages)
        

        self.setLayout(self.v_box)
        self.show()

    def send_messages(self,qoldiq):
        massa = int(self.massa.text())
        text = self.edit_text.text()
        narx = int(self.narx.text())
        hisob = massa*narx
        qoldiq = qoldiq + massa

        with open("ombor.txt", "a") as file:
            file.write(f"{text};{hisob}\n")
            if qoldiq == 0:
                self.edit_text.text("Qolmagan")


        self.edit_text.clear()
        self.massa.clear()
        self.narx.clear()





    def send_message(self,qoldiq):
        massa = int(self.massa.text())
        text = self.edit_text.text()
        narx = int(self.narx.text())
        hisob = massa*narx
        qoldiq = qoldiq - massa

        with open("ombor.txt", "a") as file:
            file.write(f"{text};{hisob}\n")
            if qoldiq == 0:
                self.edit_text.text("Qolmagan")

        self.edit_text.clear()
        self.massa.clear()
        self.narx.clear()
    
        self.read_messages(self)

    

    def read_messages(self):
        while True:
            with open("ombor.txt", "r") as file:
                msgs = file.readlines()

            self.messages.clear()
            for item in msgs:
                text,hisob = item.split(";")
                self.messages.addItem(f"{text} > {hisob}")
                file.close()

            import time
            time.sleep(1)


if __name__ == "__main__":
    app = QApplication([])
    win = ChatWindow()
    sys.exit(app.exec_())
