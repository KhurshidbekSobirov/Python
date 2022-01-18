from PyQt5.QtWidgets import QPushButton


class GameButton(QPushButton):
    __number = int()

    def __init__(self, num):
        super().__init__()

        self.__number = num
        if self.__number != 0:
            self.setText(f"{self.__number}")
        else:
            self.setText(" ")
            self.setDisabled(True)

    def get_number(self):
        return self.__number

    def __str__(self):
        return f"{self.__number}"
