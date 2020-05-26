from PySide2.QtWidgets import QLabel, QWidget, QTextEdit, QPushButton, QApplication, QGridLayout


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("IHM")
        self.layout = QGridLayout()

        self.w1 = QLabel('Laisser un commentaire')
        self.w2 = QTextEdit()
        self.w3 = QPushButton('Success')
        self.w4 = QPushButton('Cancel')

        self.layout.addWidget(self.w1, 0, 0, 1, 2)
        self.layout.addWidget(self.w2, 1, 0, 1, 2)
        self.layout.addWidget(self.w3, 2, 0, 1, 1)
        self.layout.addWidget(self.w4, 2, 1, 1, 1)

        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication([])
    win = Window()
    win.show()
    app.exec_()
