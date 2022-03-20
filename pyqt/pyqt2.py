from PyQt5 import QtWidgets
import sys
def Pencere():
    app=QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("Pyqt2")
    buton=QtWidgets.QPushButton(pencere)
    buton.setText("Burası bir butondur.")
    etiket=QtWidgets.QLabel(pencere)
    etiket.setText("Hello World")
    etiket.move(200,30)
    buton.move(190,50)
    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec_())
Pencere()