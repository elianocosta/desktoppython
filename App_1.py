from PyQt5 import QtCore, QtGui, QtWidgets,uic
#""" pyqt5_tools """
class MyWindow(QtWidgets.QMainWindow):
    def __init__(self) :
        super(MyWindow,self).__init__()
        uic.loadUi('serial_layout.ui',self)
    
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())