import sys
from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout
class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.checkbox=QCheckBox("Python is the best")
        self.yazi_alani=QLabel("")
        self.buton=QPushButton("I Agree")

        v_box=QVBoxLayout()
        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)
        self.setWindowTitle("Check Box")
        self.buton.clicked.connect(lambda: self.click(self.checkbox.isChecked(),self.yazi_alani))
        self.show()
    def click(self,checkbox,yazi_alani):
        if checkbox:
            yazi_alani.setText("Wondeful chose!!")
        else:
            yazi_alani.setText("Whats wrong with you!!")
app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())
    