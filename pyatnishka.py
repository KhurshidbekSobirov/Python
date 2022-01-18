import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from game_button import GameButton


class MainBoard(QWidget):
    __labels = [i for i in range(16)]

    def __init__(self):
        super(MainBoard, self).__init__()
        self.grid = QGridLayout()

        positions = [(x, y) for x in range(4) for y in range(4)]
        self.btn_list = [GameButton(i) for i in self.__labels]

        for btn, pos in zip(self.btn_list, positions):
            self.grid.addWidget(btn, *pos)
            btn.clicked.connect(self.movement)



        self.setLayout(self.grid)
        self.show()

    def movement(self):
        selected_btn = self.sender()
        if self.btn_list[selected_btn.get_number() - 1].get_number() == 0 or self.btn_list[selected_btn.get_number() + 1].get_number() == 0:
            c = self.btn_list[selected_btn.get_number() - 1]
            self.btn_list[selected_btn.get_number() - 1] = selected_btn
            self.btn_list[selected_btn.get_number()] = c

        elif self.btn_list[selected_btn.get_number() - 4].get_number() == 0 or self.btn_list[selected_btn.get_number() + 4].get_number() == 0:
            c = self.btn_list[selected_btn.get_number() - 4]
            self.btn_list[selected_btn.get_number() - 4] = selected_btn
            self.btn_list[selected_btn.get_number()] = c

            positions = [(x, y) for x in range(4) for y in range(4)]
            for btn, pos in zip(self.btn_list, positions):
                self.grid.addWidget(btn, *pos)
                btn.clicked.connect(self.movement)


if __name__ == '__main__':
    app = QApplication([])
    win = MainBoard()
    sys.exit(app.exec_())
