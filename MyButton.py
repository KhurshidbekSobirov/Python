from PyQt5.QtWidgets import QPushButton

class MyButton(QPushButton):

    def __init__(self, position1,position2, i, v):
        super().__init__()
        self.position2 = position1
        self.position2 = position2

        self.setGeometry(i, v)

        self.setText(-1)

    def setText(self, text: int):
        if text == 1:
            super().setText("X")
            self.setDisabled(True)

        if text == 0:
            super().setText("0")
            self.setDisabled(True)
        elif text == -1:
            super().setText("")

    def setGeometry(self, i, v):
        self.setMaximumSize(90 * i + 20)
        self.setMaximumSize(90 * v + 20)
        self.setMaximumWidth(80)
        self.maximumHeight(80)
