import sys
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QVBoxLayout,QRadioButton
class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.radio_yazisi=QLabel("Hangi dil en iyisi: ")
        self.java=QRadioButton("Java")
        self.python=QRadioButton("Python")
        self.cpp=QRadioButton("Cpp")

        self.yazi_alani=QLabel("")
        self.buton=QPushButton("Gonder")
        
        v_box=QVBoxLayout()
        v_box.addWidget(self.radio_yazisi)
        v_box.addWidget(self.java)
        v_box.addWidget(self.python)
        v_box.addWidget(self.cpp)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)
        self.setLayout(v_box)
        
        self.setWindowTitle("Radio Button")
        self.buton.clicked.connect(lambda : self.click(self.python.isChecked(),self.java.isChecked(),self.cpp.isChecked(),self.yazi_alani))
        self.show()
    def click(self,python,java,cpp,yazi_alani):
        if python:
            yazi_alani.setText("Python")
        if java:
            yazi_alani.setText("Java")
        if cpp:
            yazi_alani.setText("Cpp")

app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())
