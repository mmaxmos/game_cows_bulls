import sys
from PyQt6.QtWidgets import (QMainWindow, QApplication, QLabel, QLineEdit,
                             QVBoxLayout, QWidget, QMessageBox)
from PyQt6.QtCore import Qt
from PyQt6 import QtGui
from random import choice
from time import time


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('Bulls and Cows')
        self.resize(400, 300)
        self.setWindowIcon(QtGui.QIcon('Cow.png'))

        self.label = QLabel('Enter a four-digit number:')
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        self.label2 = QLabel('Cow - the digit is out of place.\nBull - the digit in its place.')
        self.label2.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        self.input = QLineEdit(self)
        self.input.setMaxLength(4)
        self.input.returnPressed.connect(self.enter_number)
        self.input.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.label2)

        container = QWidget()
        container.setLayout(layout)

        self.msg = QMessageBox()

        self.setCentralWidget(container)

    def enter_number(self):
        global x, k, t, s
        if len(x) == 0:
            numbers = '0123456789'
            x = choice(numbers[1:10])
            for i in range(3):
                numbers = ''.join(numbers.split(x[i]))
                x += choice(numbers)
        y = self.input.text()
        self.input.clear()
        b = 0
        if len(y) == 4:
            b = 0
            c = 0
            for i in range(4):
                if x[i] == y[i]:
                    b += 1
                elif x[i] in y:
                    c += 1
            k += 1
            s += str(k) + '. Your number: ' + str(y) + \
                ': Cows = ' + str(c) + ', Bulls = ' + str(b) + '\n'
            self.label2.setText(s)
        if b == 4:
            self.msg.setText('You win in ' + str(k) + ' steps and ' +
                             str(round(time() - t)) + ' seconds.')
            self.msg.setWindowTitle('You win!')
            self.msg.show()
            s = ''
            k = 0
            x = ''
            t = time()
            self.label2.setText('New game!')


if __name__ == "__main__":
    x = ''
    s = ''
    k = 0
    t = time()
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
