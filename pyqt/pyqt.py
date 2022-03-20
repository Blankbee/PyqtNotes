import sys
from PyQt5 import QtWidgets,QtGui
def Pencere():
    app=QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("Pyqt dersi")
    etiket1=QtWidgets.QLabel(pencere)
    etiket1.setText("Burası bir yazıdır.")
    etiket1.move(200,30)
    etiket2=QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("pythonn.png"))
    etiket2.move(150,50)
    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec_())
Pencere()