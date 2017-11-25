# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'examen.ui'
#
# Created: Thu Jun 19 10:51:46 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form2(object):
    def setupUi(self, Form2):
        Form2.setObjectName(_fromUtf8("Form2"))
        Form2.setWindowModality(QtCore.Qt.ApplicationModal)
        Form2.resize(641, 670)
        Form2.setMaximumSize(QtCore.QSize(1600, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form2.setPalette(palette)
        Form2.setStyleSheet(_fromUtf8("#examen{\n"
"background: white;\n"
"border-radius: 40 px;\n"
"min-width: 200px;\n"
"max-width: 200px;\n"
"}\n"
"#Form2{\n"
"border:2px solid #1e2bd4;\n"
"border-radius: 1 px;\n"
"background: white;\n"
"}\n"
"\n"
"#Tab_frame{\n"
"border: 2px solid #1e2bd4;\n"
"border-radius:7px;\n"
"background:#d0e4ff;\n"
"}\n"
"#Botton_frame{\n"
"border: 2px solid #1e2bd4;\n"
"border-radius:7px;\n"
"background:#d0e4ff;\n"
"\n"
"}\n"
"#Topframe{\n"
"border: 2px solid #1e2bd4;\n"
"border-radius:7px;\n"
"background:#d0e4fe;\n"
"\n"
"}\n"
"#frame_2{\n"
"border:2px solid #1e2bd4;\n"
"border-radius: 1 px;\n"
"background: white;\n"
"}\n"
"#label1_frame{\n"
"background:#8bf;\n"
"border:1px solid #1e2bd4;\n"
"border-radius:7px\n"
"}\n"
"#label2_frame{\n"
"background:#8bf;\n"
"border:1px solid #1e2bd4;\n"
"border-radius:7px\n"
"}\n"
"\n"
"\n"
"QLineEdit {\n"
"\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid #1e2bd4;\n"
"border-radius: 8px;\n"
"}\n"
"QPushButton {\n"
"color: #1e2bd4;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #1e2bd4, stop: 0.1 #1e2bd4, stop: 0.70#1e2bd4, stop: 0.5 #1e2bd4, stop: 1 #1e2bd4);\n"
"border-width: 1px;\n"
"border-color: #1e2bd4;\n"
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
"\n"
"QTableWidget{\n"
"background:#d0e4fe;\n"
"border-color:#1e2bd4;\n"
"border-width: 2px ;\n"
"border-style: solid ;\n"
"border-radius: 10;\n"
"padding:4px;\n"
"padding-left:4px;\n"
"padding-right:4px;\n"
"}"))
        self.Topframe = QtGui.QFrame(Form2)
        self.Topframe.setGeometry(QtCore.QRect(0, 0, 641, 45))
        self.Topframe.setMaximumSize(QtCore.QSize(16777215, 16777071))
        self.Topframe.setStyleSheet(_fromUtf8("#Topframe{background-color:#ffffff;\n"
"}"))
        self.Topframe.setFrameShape(QtGui.QFrame.StyledPanel)
        self.Topframe.setFrameShadow(QtGui.QFrame.Raised)
        self.Topframe.setObjectName(_fromUtf8("Topframe"))
        self.label = QtGui.QLabel(self.Topframe)
        self.label.setGeometry(QtCore.QRect(30, 11, 491, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color:#1e2bd4"))
        self.label.setObjectName(_fromUtf8("label"))
        self.frame_2 = QtGui.QFrame(Form2)
        self.frame_2.setGeometry(QtCore.QRect(0, 50, 641, 619))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.Botton_frame = QtGui.QFrame(self.frame_2)
        self.Botton_frame.setGeometry(QtCore.QRect(10, 10, 619, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Botton_frame.setFont(font)
        self.Botton_frame.setStyleSheet(_fromUtf8("#Botton_frame{background-image:url(\"/root/application/images/fond.bmp\");\n"
"}"))
        self.Botton_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.Botton_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.Botton_frame.setObjectName(_fromUtf8("Botton_frame"))
        self.label_3 = QtGui.QLabel(self.Botton_frame)
        self.label_3.setGeometry(QtCore.QRect(50, 30, 182, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color:#ffffff"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_3 = QtGui.QLineEdit(self.Botton_frame)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(280, 30, 146, 29))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.pushButton_8 = QtGui.QPushButton(self.Botton_frame)
        self.pushButton_8.setGeometry(QtCore.QRect(440, 30, 105, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(_fromUtf8("color:blue; background-color:white;border:2px solid blue;"))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_3 = QtGui.QPushButton(self.Botton_frame)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 80, 105, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(_fromUtf8("color:blue; background-color:white;border:2px solid blue;"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton = QtGui.QPushButton(self.Botton_frame)
        self.pushButton.setGeometry(QtCore.QRect(440, 80, 105, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("color:blue; background-color:white;border:2px solid blue;"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.Tab_frame = QtGui.QFrame(self.frame_2)
        self.Tab_frame.setGeometry(QtCore.QRect(10, 140, 619, 481))
        self.Tab_frame.setMaximumSize(QtCore.QSize(1600, 16777215))
        self.Tab_frame.setStyleSheet(_fromUtf8("#Tab_frame{background-image:url(\"/root/application/images/fond.bmp\");\n"
"}"))
        self.Tab_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.Tab_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.Tab_frame.setObjectName(_fromUtf8("Tab_frame"))
        self.label1_frame = QtGui.QFrame(self.Tab_frame)
        self.label1_frame.setGeometry(QtCore.QRect(11, 11, 591, 41))
        self.label1_frame.setStyleSheet(_fromUtf8("#label1_frame{background-image:url(\"/root/application/images/fond.bmp\");\n"
"}"))
        self.label1_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label1_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.label1_frame.setObjectName(_fromUtf8("label1_frame"))
        self.label_2 = QtGui.QLabel(self.label1_frame)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 266, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color:#ffffff"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tableWidget = QtGui.QTableWidget(self.Tab_frame)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(11, 58, 597, 173))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tableWidget.setPalette(palette)
        self.tableWidget.setStyleSheet(_fromUtf8("#tableWidget{background-color:#ffffff\n"
"}"))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.label2_frame = QtGui.QFrame(self.Tab_frame)
        self.label2_frame.setGeometry(QtCore.QRect(11, 237, 591, 41))
        self.label2_frame.setStyleSheet(_fromUtf8("#label2_frame{background-image:url(\"/root/application/images/fond.bmp\");\n"
"}"))
        self.label2_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label2_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.label2_frame.setObjectName(_fromUtf8("label2_frame"))
        self.label_4 = QtGui.QLabel(self.label2_frame)
        self.label_4.setGeometry(QtCore.QRect(200, 10, 189, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color:#ffffff"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tableWidget_2 = QtGui.QTableWidget(self.Tab_frame)
        self.tableWidget_2.setEnabled(True)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 320, 597, 151))
        self.tableWidget_2.setStyleSheet(_fromUtf8("#tableWidget_2{background-color:#ffffff\n"
"}"))
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.lineEdit = QtGui.QLineEdit(self.Tab_frame)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(10, 280, 181, 29))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_2 = QtGui.QPushButton(self.Tab_frame)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 280, 105, 30))
        self.pushButton_2.setMinimumSize(QtCore.QSize(105, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(105, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.setStyleSheet(_fromUtf8("color:blue; background-color:white;border:2px solid blue;"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Form2)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form2.close)
        QtCore.QMetaObject.connectSlotsByName(Form2)

    def retranslateUi(self, Form2):
        Form2.setWindowTitle(QtGui.QApplication.translate("Form2", "Examine 802.11 traffic", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form2", "                                 Examine of trace file", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form2", "Name of trace file", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setText(QtGui.QApplication.translate("Form2", "Upload", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form2", "Examine", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form2", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form2", "Informations about trace file", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form2", "Available access points", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form2", "Analysis", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form2 = QtGui.QWidget()
    ui = Ui_Form2()
    ui.setupUi(Form2)
    Form2.show()
    sys.exit(app.exec_())

