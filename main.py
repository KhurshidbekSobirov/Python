import sys
from PyQt5 import QtWidgets


class newWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        self.edit = QtWidgets.QLineEdit()


        self.h_box = QtWidgets.QHBoxLayout()
        self.v_box1 = QtWidgets.QVBoxLayout()
        self.v_box2 = QtWidgets.QVBoxLayout()
        self.v_box3 = QtWidgets.QVBoxLayout()

        self.btn10 = QtWidgets.QPushButton()
        self.btn11 = QtWidgets.QPushButton()
        self.btn12 = QtWidgets.QPushButton()
        self.btn13 = QtWidgets.QPushButton()
        self.btn14 = QtWidgets.QPushButton()
        self.btn15 = QtWidgets.QPushButton()
        self.btn16 = QtWidgets.QPushButton()
        self.btn17 = QtWidgets.QPushButton()
        self.btn18 = QtWidgets.QPushButton()

        self.v_box1.addWidget(self.btn10)
        self.v_box1.addWidget(self.btn11)
        self.v_box1.addWidget(self.btn12)

        self.v_box2.addWidget(self.btn13)
        self.v_box2.addWidget(self.btn14)
        self.v_box2.addWidget(self.btn15)

        self.v_box3.addWidget(self.btn16)
        self.v_box3.addWidget(self.btn17)
        self.v_box3.addWidget(self.btn18)

        self.h_box.addLayout(self.v_box1)
        self.h_box.addLayout(self.v_box2)
        self.h_box.addLayout(self.v_box3)


        self.btn10.clicked.connect(self.work1)
        self.btn11.clicked.connect(self.work1)
        self.btn12.clicked.connect(self.work1)
        self.btn13.clicked.connect(self.work1)
        self.btn14.clicked.connect(self.work1)
        self.btn15.clicked.connect(self.work1)
        self.btn16.clicked.connect(self.work1)
        self.btn17.clicked.connect(self.work1)
        self.btn18.clicked.connect(self.work1)

        self.btn11.clicked.connect(self.work)
        self.btn11.clicked.connect(self.work)
        self.btn12.clicked.connect(self.work)
        self.btn13.clicked.connect(self.work)
        self.btn14.clicked.connect(self.work)
        self.btn15.clicked.connect(self.work)
        self.btn16.clicked.connect(self.work)
        self.btn17.clicked.connect(self.work)
        self.btn18.clicked.connect(self.work)


        self.setLayout(self.h_box)
        self.show()

    def work(self):
        self.btn0.setText("X")



    def work1(self):
        self.btn10.setText("0")



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = newWindow()
    sys.exit(app.exec_())
