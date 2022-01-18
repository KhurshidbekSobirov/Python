import sys

from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QListWidget, QVBoxLayout ,QTextEdit, QLineEdit, QHBoxLayout, QFileDialog





class mainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.edit = QTextEdit()
        self.send_btn = QPushButton("Send")
        self.line = QLineEdit()
        self.linee = QLineEdit()
        self.h_box = QHBoxLayout()
        self.lst = QListWidget()

        self.line.setPlaceholderText("Birinchi o'yinchini: ")
        self.linee.setPlaceholderText("Enter message here...  ")



        self.layout.addWidget(self.line)
        self.layout.addWidget(self.lst)
        self.h_box.addWidget(self.linee)
        self.h_box.addWidget(self.send_btn)
        self.layout.addLayout(self.h_box)

        self.setLayout(self.layout)

        self.show()























if __name__ == ("__main__"):
    app = QApplication([])
    new = mainWindow()
    sys.exit(app.exec_())