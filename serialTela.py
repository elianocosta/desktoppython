import sys
from PyQt5 import QtCore, QtGui, QtWidgets
#from gui import *


class Ui_SGC(object):
    def setupUi(self, SGC):
        SGC.setObjectName("SGC")
        SGC.setWindowModality(QtCore.Qt.WindowModal)
        SGC.resize(821, 550)
        SGC.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(SGC)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 10, 821, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.itens_background = QtWidgets.QWidget(self.centralwidget)
        self.itens_background.setGeometry(QtCore.QRect(0, 0, 821, 16))
        self.itens_background.setAutoFillBackground(True)
        self.itens_background.setObjectName("itens_background")
        self.horizontalGroupBox = QtWidgets.QGroupBox(self.itens_background)
        self.horizontalGroupBox.setGeometry(QtCore.QRect(0, 0, 821, 511))
        self.horizontalGroupBox.setObjectName("horizontalGroupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalGroupBox)

        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.response_frame = QtWidgets.QFrame(self.centralwidget)
        self.response_frame.setGeometry(QtCore.QRect(490, 10, 331, 491))
        self.response_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.response_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.response_frame.setLineWidth(3)
        self.response_frame.setObjectName("response_frame")
        self.scrollArea = QtWidgets.QScrollArea(self.response_frame)
        self.scrollArea.setGeometry(QtCore.QRect(1, 1, 1, 1))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 16, 16))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.Response = QtWidgets.QLabel(self.response_frame)
        self.Response.setGeometry(QtCore.QRect(0, 10, 331, 20))
        self.Response.setAutoFillBackground(True)
        self.Response.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Response.setAlignment(QtCore.Qt.AlignCenter)
        self.Response.setObjectName("Response")
        self.tableView = QtWidgets.QTableView(self.response_frame)
        self.tableView.setGeometry(QtCore.QRect(10, 30, 321, 461))
        self.tableView.setObjectName("tableView")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(0, 40, 311, 461))
        self.listView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listView.setObjectName("listView")
        self.command_buttons_label = QtWidgets.QLabel(self.centralwidget)
        self.command_buttons_label.setGeometry(QtCore.QRect(0, 20, 311, 20))
        self.command_buttons_label.setAutoFillBackground(True)
        self.command_buttons_label.setAlignment(QtCore.Qt.AlignCenter)
        self.command_buttons_label.setObjectName("command_buttons_label")
        self.checkBox_zero = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_zero.setGeometry(QtCore.QRect(10, 50, 70, 17))
        self.checkBox_zero.setText("")
        self.checkBox_zero.setObjectName("checkBox_zero")
        self.pushButton_zero = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_zero.setGeometry(QtCore.QRect(30, 50, 75, 23))
        self.pushButton_zero.setObjectName("pushButton_zero")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(30, 90, 75, 23))
        self.pushButton_1.setObjectName("pushButton_1")
        self.checkBox_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_1.setGeometry(QtCore.QRect(10, 90, 70, 17))
        self.checkBox_1.setText("")
        self.checkBox_1.setObjectName("checkBox_1")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(90, 450, 131, 23))
        self.pushButton_add.setDefault(False)
        self.pushButton_add.setObjectName("pushButton_add")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(318, 40, 171, 22))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 20, 151, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.listView.raise_()
        self.line.raise_()
        self.itens_background.raise_()
        self.response_frame.raise_()
        self.command_buttons_label.raise_()
        self.checkBox_zero.raise_()
        self.pushButton_zero.raise_()
        self.pushButton_1.raise_()
        self.checkBox_1.raise_()
        self.pushButton_add.raise_()
        self.comboBox.raise_()
        self.label.raise_()
        SGC.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SGC)
        self.statusbar.setObjectName("statusbar")
        SGC.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(SGC)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 21))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuRun = QtWidgets.QMenu(self.menubar)
        self.menuRun.setObjectName("menuRun")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        SGC.setMenuBar(self.menubar)
        self.actionNew_File = QtWidgets.QAction(SGC)
        self.actionNew_File.setObjectName("actionNew_File")
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(SGC)
        QtCore.QMetaObject.connectSlotsByName(SGC)

    def retranslateUi(self, SGC):
        _translate = QtCore.QCoreApplication.translate
        SGC.setWindowTitle(_translate("SGC", "SGC"))
        self.scrollArea.setAccessibleName(_translate("SGC", "response_scroll_area"))
        self.Response.setText(_translate("SGC", "Reponse Device"))
        self.command_buttons_label.setText(_translate("SGC", "Commands buttons"))
        self.pushButton_zero.setText(_translate("SGC", "PushButton"))
        self.pushButton_1.setText(_translate("SGC", "PushButton"))
        self.pushButton_add.setText(_translate("SGC", "Add Comand Button"))
        self.label.setText(_translate("SGC", "COM & LTP Ports"))
        self.menuArquivo.setTitle(_translate("SGC", "File"))
        self.menuEdit.setTitle(_translate("SGC", "Edit"))
        self.menuRun.setTitle(_translate("SGC", "Run"))
        self.menuTools.setTitle(_translate("SGC", "Tools"))
        self.actionNew_File.setText(_translate("SGC", "New File"))


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self) :
        super(MyWindow,self).__init__()
        self.ui = Ui_SGC()
        self.ui.setupUi(self)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
    
    