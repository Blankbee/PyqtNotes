from PyQt5 import QtWidgets
import sys
def Pencere():
    app=QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("Pyqt3")
    okay=QtWidgets.QPushButton("Tamam")
    cancel=QtWidgets.QPushButton("Iptal")
    #h_box=QtWidgets.QHBoxLayout()
    #h_box.addWidget(okay)
    #h_box.addStretch()               HORIZANTAL BIR BOX BOLGESI OLUSTURDUK ICINE BUTON YAZI EKLENEBILIR
    #h_box.addWidget(cancel)
    #pencere.setLayout(h_box)
    h_box=QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(okay)
    h_box.addWidget(cancel)
    v_box=QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)
    #v_box=QtWidgets.QVBoxLayout()
    #v_box.addStretch()
    #v_box.addWidget(okay)#             VERTICAL BOX BOLMESI ....
    #v_box.addWidget(cancel)
    pencere.setLayout(v_box) #ikisini iç içe yazıp butonları sağ aşağı alıyoruz
    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec_())
Pencere()