from PySide2.QtWidgets import QWidget
# from PySide2.QtGui import

class progress(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setFixedSize(400, 300)
        self.setWindowTitle("IHM")
