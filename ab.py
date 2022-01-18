import sys, threading
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit


class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.btn_send = QPushButton("Send")
        self.edit_name = QLineEdit()
        self.edit_text = QLineEdit()
        self.messages = QListWidget()

        self.h_box.addWidget(self.edit_text)
        self.h_box.addWidget(self.btn_send)

        self.v_box.addWidget(self.edit_name)
        self.v_box.addWidget(self.messages)
        self.v_box.addLayout(self.h_box)

        self.edit_name.setPlaceholderText("Your name")
        self.edit_text.setPlaceholderText("Enter message here...")

        self.btn_send.clicked.connect(self.send_message)
        threading.Thread(target=self.read_messages).start()

        self.setLayout(self.v_box)
        self.show()

    def send_message(self):
        name = self.edit_name.text()
        text = self.edit_text.text()

        with open("messages.dat", "a") as file:
            file.write(f"{name};{text}\n")

        self.edit_text.clear()

    def read_messages(self):
        while True:
            with open("messages.dat", "r") as file:
                msgs = file.readlines()

            self.messages.clear()
            for item in msgs:
                sender, text = item.split(";")
                self.messages.addItem(f"{sender} > {text[:-1]}")

            import time
            time.sleep(1)


if __name__ == "__main__":
    app = QApplication([])
    win = ChatWindow()
    sys.exit(app.exec_())