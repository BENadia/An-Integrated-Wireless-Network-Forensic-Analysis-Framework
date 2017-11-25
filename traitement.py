# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'traitement.ui'
#
# Created: Sun Jun 15 22:08:37 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form3(object):
    def setupUi(self, Form3):
        Form3.setObjectName(_fromUtf8("Form3"))
        Form3.resize(634, 216)
        Form3.setStyleSheet(_fromUtf8("#top_Frame{\n"
"border: 2px solid #1e2bd4;\n"
"border-radius:7px;\n"
"background:#d0e4fe;\n"
"}\n"
"#Form3{\n"
"border:2px solid #1e2bd4;\n"
"border-radius: 1 px;\n"
"background: white;\n"
"}\n"
"QLineEdit {\n"
"\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid #1e2bd4;\n"
"border-radius: 8px;\n"
"}\n"
"QPushButton {\n"
"color: black;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0  #1e2bd4, stop: 0.1  #1e2bd4, stop: 0.70 #1e2bd4, stop: 0.5  #1e2bd4, stop: 1  #1e2bd4);\n"
"border-width: 1px;\n"
"border-color: #200;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 6px;\n"
"\n"
"padding-left: 6px;\n"
"padding-right: 5px;\n"
"min-width: 90px;\n"
"max-width: 90px;\n"
"min-height: 14px;\n"
"max-height: 14px;\n"
"}\n"
"QComboBox{\n"
"color:#1e2bd4;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color:#1e2bd4;\n"
"}"))
        self.bottom_frame = QtGui.QFrame(Form3)
        self.bottom_frame.setGeometry(QtCore.QRect(10, 50, 611, 153))
        self.bottom_frame.setStyleSheet(_fromUtf8("#bottom_frame{background-image:url(\"/root/application/images/fond.bmp\");\n"
"}"))
        self.bottom_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.bottom_frame.setObjectName(_fromUtf8("bottom_frame"))
        self.gridLayout = QtGui.QGridLayout(self.bottom_frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.bottom_frame)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.pushButton_2 = QtGui.QPushButton(self.bottom_frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(_fromUtf8("color:blue; background-color:white;border:2px solid blue"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 4, 1, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.bottom_frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(_fromUtf8("color:blue; background-color:white;border:2px solid blue"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 4, 2, 1, 2)
        self.label_3 = QtGui.QLabel(self.bottom_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.bottom_frame)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 2)
        self.pushButton = QtGui.QPushButton(self.bottom_frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("color:blue; background-color:white;border:2px solid blue"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 3, 1, 1)
        self.comboBox = QtGui.QComboBox(self.bottom_frame)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 2)
        self.label_2 = QtGui.QLabel(self.bottom_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color:#ffffff;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.top_Frame = QtGui.QFrame(Form3)
        self.top_Frame.setGeometry(QtCore.QRect(0, 0, 631, 45))
        self.top_Frame.setStyleSheet(_fromUtf8("background-color:#ffffff"))
        self.top_Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.top_Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.top_Frame.setObjectName(_fromUtf8("top_Frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.top_Frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_4 = QtGui.QLabel(self.top_Frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color:#1e2bd4;"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.retranslateUi(Form3)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), Form3.close)
        QtCore.QMetaObject.connectSlotsByName(Form3)

    def retranslateUi(self, Form3):
        Form3.setWindowTitle(QtGui.QApplication.translate("Form3", "Launch analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form3", "BSSID", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form3", "Launch", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form3", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form3", "Name of trace file", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form3", "Upload", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Form3", "--------------------", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Form3", "WEP attack", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("Form3", "DoS attack", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("Form3", "EVIL TWIN attack", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("Form3", "All attacks", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form3", "Type of attack", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form3", "                                     Analysis of trace file", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form3 = QtGui.QWidget()
    ui = Ui_Form3()
    ui.setupUi(Form3)
    Form3.show()
    sys.exit(app.exec_())

